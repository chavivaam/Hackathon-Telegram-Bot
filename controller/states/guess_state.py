# from bot import *
from controller.states.finish_state import FinishState
import requests
from utils.config import *
from utils.constants import GUESS_STATE, BAD_GUESS , GOOD_GUESS
from model.bot_responses_model import return_user_message

class GuessState():

    def __init__(self, artist_name, item_number , channel_id ):

        self.artist_name = artist_name
        self.item_number = item_number
        self.channel_id = channel_id
        

    def handle_message(self, msg, bot):

        res = self.check_user_guess(msg.get_text())
        if res:
            message = return_user_message(GUESS_STATE, GOOD_GUESS)
            bot.handle_state(FinishState())
        else:
            message = return_user_message(GUESS_STATE, BAD_GUESS)
        
        return message

    def check_user_guess(self, user_guess):


        request_url = BASE_YOUTUBE_API_URL+'search?key={}&channelId={}&part=snippet,id&order=date&maxResults=20'.format(API_KEY,self.channel_id)

        result_data = requests.get(request_url).json()

        if user_guess == "":
            return False

        user_guess_arr = user_guess.lower().split(" ")
        audio_title_arr = result_data['items'][self.item_number]['snippet']['title'].lower().split(" ")
        artist_name_arr = self.artist_name.lower().split(" ")


        for word in user_guess_arr:
            if word not in audio_title_arr:
                return False
            if word in artist_name_arr:
                return False

        return True


