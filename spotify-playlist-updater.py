import time
import schedule
import spotipy
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

import base64

print("Starting Playlist updater")

def func():
    scope = 'playlist-modify-public playlist-modify-private ugc-image-upload'

    # Spotify Username
    username = 'username'

    # Spotify Developer App Client ID and Secret ID
    SPOTIPY_CLIENT_ID = 'clientid'
    SPOTIPY_CLIENT_SECRET = 'clientsecret'

    token = util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,redirect_uri='Redirected URI')
    sp = spotipy.Spotify(auth=token)

    # Playlist 1 Data
    id = 'https://open.spotify.com/playlist/yourplaylist1'
    results = sp.playlist(id)
    playlist_name = 'Playlist Name 1'
    playlist_description = 'Playlist Desc 1'

    # Playlist 2 Data
    id2 = 'https://open.spotify.com/playlist/yourplaylist2'
    results2 = sp.playlist(id2)
    playlist_name2 = 'Playlist Name 2'
    playlist_description2 = 'Playlist Desc 2'





    # Get the time
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    

    # Check if playlist 1 has been taken down
    if playlist_name != (results["name"]):
        
        # If yes, update the details
        with open(r"C:\Users\You\YourWorkingDirectory\Data\PlaylistPhoto1.jpeg", "rb") as img_file:
         myimage = base64.b64encode(img_file.read())
        image_b64 = myimage
        
        sp.playlist_upload_cover_image(playlist_id=id, image_b64 = myimage)
        sp.user_playlist_change_details(username, id, name=playlist_name, description=playlist_description)
        
        # Timestamp
        print(current_time, " - playlist 1 restored")

    else:
        # If no, do nothing, just print a timestamp
        print(current_time, " - playlist 1 ok")



    # Check if playlist 2 has been taken down
    if playlist_name2 != (results2["name"]):
        
        # If yes, update the details
        with open(r"C:\Users\You\YourWorkingDirectory\Data\PlaylistPhoto2.jpeg", "rb") as img_file:
         myimage2 = base64.b64encode(img_file.read())
        image_b64 = myimage2
        
        sp.playlist_upload_cover_image(playlist_id=id2, image_b64 = myimage2)
        sp.user_playlist_change_details(username, id2, name=playlist_name2, description=playlist_description2)
        
        # Timestamp
        print(current_time, " - playlist 2 restored")

    else:
        # If no, do nothing, just print a timestamp
        print(current_time, " - playlist 2 ok")







        
# Schedule
func()
schedule.every(5).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(30)
    continue 
