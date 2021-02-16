from model.bot_responses_model import *
from controller.states.choose_artist_state import ChooseArtistState
from utils.constants import START_STATE

class StartState:
    def handle_message(self, msg, bot):
        #res = get_start_response()
        message = return_user_message(START_STATE)
        bot.handle_state(ChooseArtistState())
        return message

