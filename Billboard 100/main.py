from dotenv import dotenv_values
from bs4 import BeautifulSoup
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth



cred = dotenv_values(".env")
USER_ID = cred["USER_ID"]
CLIENT_ID = cred["CLIENT_ID"]
CLIENT_SECRET = cred["CLIENT_SECRET"]
REDIRECT_URI = cred["REDIRECT_URI"]
ENDPOINT = f"https://api.spotify.com/v1/users/{USER_ID}/playlists"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=".cache",
        username=USER_ID
    )
)
user_id = sp.current_user()["id"]



year = input("What year do you want to travel to? type the date in the format YYYY-MM-DD: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(billboard_url)
billboard_web = response.text

soup = BeautifulSoup(billboard_web,"html.parser")

song_titles = [song.ul.li.h3.getText().strip() for song in soup.find_all(name="li", class_="lrv-u-width-100p") if song.ul.li.h3 is not None]
song_uri = []

for song in song_titles:
    try:
        result = sp.search(q=f"track:{song} year:{year[:4]}", type="track")
        song_uri.append(result["tracks"]["items"][0]["uri"])
        # print(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} does not exist on spotify, skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)



