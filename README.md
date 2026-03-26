
# Macindows-Rainmeter-Skin-Suite
<p align="center">
  A skin suite for Rainmeter Following the Macindows color scheme with a loose macOS9/Platinum inspiration  
  <img src="https://github.com/Lerakei-0/Macindows-Rainmeter-Skin-Suite/blob/main/Screenshot.png?raw=true" />
</p>

# Configuration
## X Followers widget
Needed: Python, Selenium  
```
pip install python selenium webdriver-manager
```
How this widget works is a python script will launch a headless selenium instance fetching your profile on nitter.net and writing its follower count in a text file, the rainmeter skin will then read this text file and show the followers count inside the widget.  
> [!NOTE]
> Take into account this widget will need to have its python script added to the windows task scheduler and automated to re-run eavery hour or so(you can choose), so this shouldn't be a skin and script to use on a lower-end pc.
### Editing the python script
Change your X username at line 12. Plain username with no @ eg "cutestscats"  
Change the output directory of the txt file, by default it will save in your rainmeter folder in Documents\Rainmeter\Temp.  
### Editing the ini file
Replace "{YOUR X USERNAME WITHOUT @}" with your plain username without @ eg "AccountName=cutestscats" at line 18.  
If you edited the output file directory in th epython script, edit it at line 26.
### Adding the python script to the Windows Task Scheduler
>- Open the windows task scheduler.  
>- Create a new task.  
>- In the general tab give your task a name, for exemple, "X followers Fetcher".  
>- In the trigger tab create a new trigger.  
>- In launch, select "At Logon" in the drop down menu.  
>- Still in the same window, at the bottom, tick "Repeat task every:", choose your desired option and then click "ok".  
>- In the actions tab click new.  
>- Action: "Launch a program".  
>- Program/Script: "%localappdata%\Python\pythoncore-3.14-64\pythonw.exe".  
>- Arguments: "\DIRECTORY WHERE YOU PLACED THE PYTHON SCRIPT\fetch_followers_selenium_headless.py".  
>- Done.

## Mastodon Followers widget
Much simpler configuration since mastodon's API are open and free.  
Simply open the .ini file and edit the following:  
- Line 18: Replace "{YOUR INSTANCE eg: mastodon.social}" with your instance url.  
- Line 19: Repalce "{YOUR USERNAME ON SAID INSTANCE}" with your plain username with no @.

Exemple:
>MastodonInstance=mastodon.social  
>MastodonUsername=Mastodon

## Slideshow widget
Simply change line 20 to your desired image folder path.
