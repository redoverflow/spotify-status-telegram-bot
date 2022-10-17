import sys
import api
import time
from pyrogram import Client
from pyrogram.raw import functions
import simplejson as json

config = json.load(open("config.json", encoding="utf-8"))
sleep_time = config["sleep_time"]
prefix_suffix = [config["prefix"], config["suffix"]]

app = Client("my_account", api_id=config["api_id"], api_hash=config["api_hash"])
#app = Client("my_account")
prev_song_name = ""

def get_spotify_update():
    app_handle = api.getspotifyHandle()
    app_title = api.getWindowTitleByHandle(app_handle)

    return app_title

def song_check_loop(app, prefix_suffix):
    global prev_song_name
    song_name = get_spotify_update()
    if prev_song_name == "" or prev_song_name != song_name:
        stylized_song_name = prefix_suffix[0] + song_name + prefix_suffix[1]
        app.invoke(functions.account.UpdateProfile(about=stylized_song_name))
        prev_song_name = song_name
    else:
        prev_song_name = song_name
    time.sleep(sleep_time)

with app:
    while True:
        try:
            song_check_loop(app, prefix_suffix)
        except KeyboardInterrupt:
            print("stopping bot...")
            song_check_loop(app, prefix_suffix)
            exit()

#update_loop()