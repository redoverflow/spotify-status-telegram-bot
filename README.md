# Spotify Listening Status for Telegram
A small script I made in a day which updates your Telegram bio to the Spotify song you're currently listening to.

## Platforms
This script is only for Windows, but I'm sure it can be made cross-platform too.

## How does it work?
Luckily, Spotify just puts the current song in the window title, so we can scrape it from there. I implemented the updating by checking the title every second (bad solution i know), and if it's different, then a new song must be playing, so it changes your bio to that. I used [Pyrogram](https://github.com/pyrogram/pyrogram) to make the bot part itself, it's a really good library in my opinion.

## Setup
Since this is a bot that will run on your own account, you'll need to get the **ID and hash** for your account. You can just grab them [from Telegram](https://my.telegram.org/apps), but remember to **treat them as a secret**, since they can be used to get **access to your account** (well mostly).

Now, rename the **config.example.json** file to **config.json** in the root directory, then open it and put your ID and hash in the *api_id* and *api_hash* fields. You can also change the prefix and suffix (or what gets put before and after the song name) there.

After you've done that, you need to open a command prompt in the root directory and type `python main.py`. Since it's your first time launching the script, you'll be asked to enter the phone number linked to your Telegram account for verification, make sure to enter it **no spaces, no symbols** (e.g. +375 33 (123-45-67) becomes 375331234567).
You'll either receive an SMS to your phone or a message on the Telegram app telling you a code, you should enter it into the command prompt. And now you're done! You can fire up Spotify and Telegram to see your bio magically change to the song you are listening to currently.

