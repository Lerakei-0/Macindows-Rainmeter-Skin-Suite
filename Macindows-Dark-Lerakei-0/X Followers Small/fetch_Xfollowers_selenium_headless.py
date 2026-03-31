#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
from datetime import datetime
import re

USERNAME = "{YOUR-USERNAME-NO-@}"
OUTPUT_FILE = os.path.expanduser("~\\Documents\\Rainmeter\\temp\\followers.txt")

def get_followers_selenium():
    """Use Selenium with headless Chrome to fetch follower count"""
    
    print("Launching headless Chrome browser...")
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-web-resources")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    try:
        # Try to use installed chromedriver
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except:
            # If that fails, try webdriver-manager
            print("Trying webdriver-manager...")
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
        
        url = "https://nitter.net/" + USERNAME
        print("Loading: " + url)
        driver.get(url)
        
        print("Waiting for page to load (5 seconds)...")
        time.sleep(5)
        
        # Try to find follower count
        print("Looking for profile stats...")
        
        # Method 1: Look for profile-stat-num elements
        stats = driver.find_elements(By.CLASS_NAME, "profile-stat-num")
        print("Found " + str(len(stats)) + " stat elements")
        
        if len(stats) >= 3:
            # Followers is usually the 3rd stat (after tweets and following)
            followers = stats[2].text.strip()
            print("[+] Followers (method 1): " + followers)
            driver.quit()
            return followers
        
        # Method 2: Look for any text containing "Followers"
        page_text = driver.page_source
        
        # Look for patterns like "123 Followers" or "123K Followers"
        match = re.search(r'(\d+(?:[,\s]\d{3})*)\s*Followers?', page_text, re.IGNORECASE)
        if match:
            followers = match.group(1).replace(',', '').replace(' ', '')
            print("[+] Followers (method 2): " + followers)
            driver.quit()
            return followers
        
        # Method 3: Print page source to debug
        print("\n" + "="*60)
        print("Page source (first 3000 chars):")
        print("="*60)
        print(driver.page_source[:3000])
        
        driver.quit()
        return None
        
    except Exception as e:
        print("Error: " + str(e))
        import traceback
        traceback.print_exc()
        try:
            driver.quit()
        except:
            pass
        return None

def main():
    print("=" * 60)
    print("Fetching follower count for @" + USERNAME + "...")
    print("=" * 60)
    print()
    
    followers = get_followers_selenium()
    
    if not followers:
        print("\n[-] Failed to fetch follower count")
        
        if os.path.exists(OUTPUT_FILE):
            with open(OUTPUT_FILE, 'r') as f:
                cached = f.read().strip()
            if cached and cached != "N/A":
                print("Using cached value: " + cached)
                return
        
        return
    
    print("\n[+] Follower count: " + followers)
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        f.write(followers)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("[+] Saved to: " + OUTPUT_FILE)
    print("[+] Last updated: " + timestamp)
    print("=" * 60)

if __name__ == "__main__":
    main()
