
# Spotify Playlist Updater

Forked from 
https://github.com/aeriie/spotify-playlist-updater
https://github.com/mousehawk/spotify-playlist-updater


A Python script to check Spotify Playlist data for up to two playlists every 5 minutes and restore it if missing. Includes a GUI version and a standard version.

Includes two versions:

* Standard version
* GUI version (requires PySimple)

## Getting Started
#### You will need Python to execute the script:

* Python 3
    * [Installation Link](https://www.python.org/downloads/)

#### Spotify Playlist Updater with GUI requires 4 dependencies: 

#

##### Pip

* A Package Management System for Python.
* [Installation Link](https://pip.pypa.io/en/stable/installation/)
* For Windows, you can run ```py -m ensurepip --upgrade``` in CMD to install. 

##### Schedule
* Python job scheduler to run the script on a timer.
* [Installation Link](https://schedule.readthedocs.io/en/stable/installation.html)
* For Windows, you can run ```-m pip install schedule --upgrade``` in CMD to install. 

##### Spotipy
* Python library for the Spotify Web API
* [Installation Link](https://spotipy.readthedocs.io/en/2.19.0/#installation)
* For Windows, you can run ``` py -m pip install spotipy --upgrade ``` in CMD to install. 

##### PySimple
* Python GUI
* [Installation Link](https://pypi.org/project/PySimpleGUI/)
* For Windows, you can run ``` pip install PySimpleGUI ``` in CMD to install. 

##### A Web Domain

* No website required, only a web domain for redirecting the API request and retrieving the user authorization token. 
* If you don't already own a domain, you can create one at [https//wix.com](https://wix.com)


### Set Up

##### Installing the Script

* Install the dependencies listed above. 
* Choose a location on your device (I'll refer to this as the working directory)
* Download the latest release to the working directory. 
* Save your playlist photo (if applicable) in the ``data`` folder of the working directory
    * The photo must be 150KB or less. If it is too large, resize the photo. 
    * You can use this website to resize your image: https://www.resizepixel.com/reduce-image-in-kb/

##### Set up Client ID, Client Secret and Redirect URI
* Login to Spotify Developer Account
    * Go to https://developer.spotify.com/dashboard/ and click Manage Dashboard. 
    * Then, sign in with your Spotify credentials and accept the latest Developer terms of service.
    * Note your Client ID, and Client Secret. 
* Create an App
    * In the Developer Dashboard, create an App. You can put whatever you'd like for the App name and description. 
    * Click Edit Settings. 
        * Add your domain address to the Redirected URI's field, and click Add. Make sure to Save. 

### Standard Version
####  Adding your Playlist information
* Right click \spotify-playlist-updater.py from the working directory, and select "Edit with IDLE"
   * Put your Playlist Image path in place of: ```` "C:\\Users\\You\\YourWorkingDirectory\\Data\\PlaylistPhoto.jpeg" ````
   * Put your Spotify Username in place of: ```` 'username' ````
   * Put your Client ID in place of ```` 'clientid' ````
   * Put your Client Secret in place of ```` 'clientsecret' ````
   * Put your Web Domain Address in place of ```` 'http://yourdomain.com' ````
   * Put your Spotify Playlist Link in place of ```` 'https://open.spotify.com/playlist/yourplaylist' ````
   * Put your Playlist Description in place of ```` 'Playlist Name' ````
   * Put your Playlist Description in place of ```` 'Playlist Description' ````
* **Save the script once your changes are made.** 


#### Running the Script (Standard Version)

* Right click spotify-playlist-updater.py and Open. 
* The script updates the Playlist every 5 minutes. You can adjust the update frequency by changing the number value for ```` schedule.every(5).minutes.do(func) ````
* The script will restart if it runs into a timeout to prevent it from failing during an internet hiccup. 
    * If you have an unstable internet connection and run into issues, try removing the ```` continue ```` statement. 

### GUI Version
#### Adding your Playlist informatio
* Double-click spotify-playlist-updater-gui.py from the working directory
* Input your information into the labelled text fields.

#### Running the Script
* Click 'Submit'



## Help

* If you get an error that "Read timed out. (read timeout=5)", restart the script. 
* If your script doesnt get past "Starting Playlist Updater", run the script using IDLE:
   * Right click spotify-playlist-updater and click Edit with IDLE
   * Click F5 to run the script
      * Let the script run. Any errors will be listed as the script encounters them. 
* GUI version: the window may show "Not Responding", but the script will still run. Working on addressing this in a later update. The GUI version is meant to be a relatively accessible introduction point for playlist curators with limited technical background to protect their playlists. The standard  version is currently more efficient as the user does not have to manually fill text fields.


## Authors

[Aeriie](https://github.com/aeriie)
[mousehawk](https://github.com/mousehawk)
[wilu222](https://github.com/wilu222)

## Version History

* 0.1
    * Initial Release



