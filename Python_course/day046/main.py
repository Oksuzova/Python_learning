import requests
from bs4 import BeautifulSoup
import spotipy
import os
from dotenv import load_dotenv
import sys


if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")

SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

date = input("Which year do you want to travel to? Type the date in this YYY-MM-DD format: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


spotify = spotipy.oauth2.SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-public"
)
access_token = spotify.get_cached_token()

sp = spotipy.Spotify(client_credentials_manager=spotify)
songs_list = []


def search_spotify_track():
    for song in song_names:
        result = sp.search(song)
        songs_list.append(result["tracks"]["items"][0]["uri"])


def create_playlist(playlist_name, songs_uris):
    user_info = sp.current_user()
    user_id = user_info["id"]
    playlist = sp.user_playlist_create(user_id, playlist_name)
    sp.playlist_add_items(playlist["id"], songs_uris)


search_spotify_track()
create_playlist(f"{date} Billboard 100", songs_list)

# import csv
# import sys
#
# if sys.stdout.encoding != 'utf-8':
#     sys.stdout.reconfigure(encoding='utf-8')
#
#
# def parse_data_from_file():
#
#     sentences = []
#     labels = []
#
#     with open("training_cleaned.csv", encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         for el in reader:
#             labels.append(int(int(el[0])/4))
#             sentences.append(el[5])
#
#     return sentences, labels
#
#
# print(parse_data_from_file())
