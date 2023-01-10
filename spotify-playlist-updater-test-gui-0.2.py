import time
import schedule
import spotipy
import json
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


import base64

import PySimpleGUI as sg

# create the form layout
form_layout = [[sg.Text('Spotify username'), sg.InputText()],
               [sg.Text('Client ID'), sg.InputText()],
               [sg.Text('Client Secret'), sg.InputText(password_char='*')],
               [sg.Text('Redirect URI'), sg.InputText()],
               [sg.Text('Playlist 1 URL'), sg.InputText()],
               [sg.Text('Playlist 1 name'), sg.InputText()],
               [sg.Text('Playlist 1 description'), sg.InputText()],
               [sg.Text('Playlist 1 image path'), sg.InputText()],
               [sg.Text('Playlist 2 URL'), sg.InputText()],
               [sg.Text('Playlist 2 name'), sg.InputText()],
               [sg.Text('Playlist 2 description'), sg.InputText()],
               [sg.Text('Playlist 2 image path'), sg.InputText()],
               [sg.Submit(), sg.Cancel()]
              ]

# create the form window
form = sg.Window('Playlist Updater', form_layout)



# event loop to process the form's events
while True:
    event, values = form.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    elif event == 'Submit':
        # update the code with the form input values
        scope = 'playlist-modify-public playlist-modify-private ugc-image-upload'
        username = values[0]
        SPOTIPY_CLIENT_ID = values[1]
        SPOTIPY_CLIENT_SECRET = values[2]
        redirect_uri = values[3]
        id = values[4]
        playlist_name = values[5]
        playlist_description = values[6]
        image_path1 = values[7]
        id2 = values[8]
        playlist_name2 = values[9]
        playlist_description2 = values[10]
        image_path2 = values[11]        

        print("Starting Playlist updater")
          
        def func():
            scope = 'playlist-modify-public playlist-modify-private ugc-image-upload'

            # Spotify Username
            username = values[0]

            # Spotify Developer App Client ID and Secret ID
            SPOTIPY_CLIENT_ID = values[1]
            SPOTIPY_CLIENT_SECRET = values[2]

            token = util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,redirect_uri=values[3])
            sp = spotipy.Spotify(auth=token)

            # Playlist 1 Data
            id = values[4]
            results = sp.playlist(id)
            playlist_name = values[5]
            playlist_description = values[6]
            image_path1 = values[7]

            # Playlist 2 Data
            id2 = values[8]
            if id2 and id2.strip():
                # If id2 is not empty, make a request to the Spotify API using the playlist URL
                results2 = sp.playlist(id2)
                playlist_name2 = values[9]
                playlist_description2 = values[10]
                image_path2 = values[11]  


            # Get the time
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            

            # Check if playlist 1 has been taken down
            if playlist_name != (results["name"]):
                
                # If yes, update the details
                with open(image_path1, "rb") as img_file:
                 myimage = base64.b64encode(img_file.read())
                image_b64 = myimage
                
                sp.playlist_upload_cover_image(playlist_id=id, image_b64 = myimage)
                sp.user_playlist_change_details(username, id, name=playlist_name, description=playlist_description)
                
                # Timestamp
                print(current_time, " - playlist 1 restored")

            else:
                # If no, do nothing, just print a timestamp
                print(current_time, " - playlist 1 ok")


            if id2 and id2.strip():  # Check if id2 is empty

                # Check if playlist 2 has been taken down
                if playlist_name2 != (results2["name"]):
                    
                    # If yes, update the details
                    with open(image_path2, "rb") as img_file:
                     myimage2 = base64.b64encode(img_file.read())
                    image_b64 = myimage2
                    
                    sp.playlist_upload_cover_image(playlist_id=id2, image_b64 = myimage2)
                    sp.user_playlist_change_details(username, id2, name=playlist_name2, description=playlist_description2)
                    
                    # Timestamp
                    print(current_time, " - playlist 2 restored")

                else:
                    # If no, do nothing, just print a timestamp
                    print(current_time, " - playlist 2 ok")

            else:
                # Skip updating the details for playlist 2
                pass





                    
        # Schedule
        func()
        schedule.every(5).minutes.do(func)
              
        while True:
            event, values = form.Read(timeout=100)
            schedule.run_pending()
            time.sleep(30)


