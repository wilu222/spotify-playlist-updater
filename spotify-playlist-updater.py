import time
import schedule
import spotipy
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

import base64

print("Starting Playlist updater")
  
def func():
    scope = 'playlist-modify-public ugc-image-upload'

    # Spotify Username
    username = '00000000000'

    # Spotify Developer App Client ID and Secret ID
    SPOTIPY_CLIENT_ID = '00000000000000000000000000000000'
    SPOTIPY_CLIENT_SECRET = '00000000000000000000000000000000'

    token = util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,redirect_uri='http://your-url.com')
    sp = spotipy.Spotify(auth=token)

    # Playlist Data
    id = 'https://open.spotify.com/playlist/0000000000000000000000'
    results = sp.playlist(id)
    playlist_name = 'Your Playlist Title'
    playlist_description = 'Your Playlist Description'
    
    # Get the time
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Check if playlist has been taken down
    if playlist_name != (results["name"]):
        
        # If yes, update the details
        with open("C:\\Users\\Work\\Documents\\Tools\\spotify-playlist-updater-main\\data\\ambient.jpg", "rb") as img_file:
         myimage = base64.b64encode(img_file.read())
        image_b64 = myimage
        
        sp.playlist_upload_cover_image(playlist_id=id, image_b64 = myimage)
        sp.user_playlist_change_details(username, id, name=playlist_name, description=playlist_description)
        
        # Timestamp
        print(current_time, " - playlist restored")

    else:
        # If no, do nothing, just print a timestamp
        print(current_time, " - ok")

func()
schedule.every(5).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(30)
    continue 
