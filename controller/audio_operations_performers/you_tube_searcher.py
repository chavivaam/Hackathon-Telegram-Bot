
import requests
import json
import random
from utils.config import *

RANDOM_RANGE = 5

def search_audio_by_artist(artist_name):

    # should get the channel id of any artist name
    res = get_audio_id("UCVOwOs8Cn4Uv0Hc2foG9YCQ")
    # UC0C-w0YjGpqDXGB8IHb662A
    # UCVOwOs8Cn4Uv0Hc2foG9YCQ
    # UCDPM_n1atn2ijUwHd0NNRQw
    # UCTX_NQXdWx-80lZBQNVu1VQ
    return res

def get_audio_id(channel_id):

    request_url = BASE_YOUTUBE_API_URL+'search?key={}&channelId={}&part=snippet,id&order=date&maxResults=20'.format(API_KEY,channel_id)
 
    result_data = requests.get(request_url).json()

    range = len(result_data['items']) if RANDOM_RANGE > len(result_data['items']) else RANDOM_RANGE

    random_number = random.randint(0, range)

    return result_data['items'][random_number]['id']['videoId'], random_number

