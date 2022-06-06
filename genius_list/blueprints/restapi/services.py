import os
import requests
from dotenv import load_dotenv


load_dotenv()

__GENIUS_BASE_URL = os.getenv("GENIUS_URL")
__GENIUS_TOKEN = os.getenv("GENIUS_TOKEN")


def search_artist(artist_name: str) -> dict:
    url: str = "".join([__GENIUS_BASE_URL, "/search?q=", artist_name])
    resp = requests.get(url, headers=__make_credentials())
    print(resp)
    if resp.status_code == 200:
        artist_id = _get_artist_id(body=resp.json())
        return get_top_songs(artist_id)
    return resp["meta"]


def get_top_songs(artist_id) -> dict:
    url: str = "".join(
        [__GENIUS_BASE_URL, f"/artists/{artist_id}/songs?sort=popularity&per_page=10"]
    )
    resp = requests.get(url, headers=__make_credentials())
    if resp.status_code == 200:
        return resp.json()["response"]
    return resp["meta"]


def _get_artist_id(body: dict):
    if not body:
        return None
    return body["response"]["hits"][0]["result"]["primary_artist"]["id"]


def __make_credentials() -> dict:
    return {"Authorization": f"Bearer {__GENIUS_TOKEN}"}
