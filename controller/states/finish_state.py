from model.bot_responses_model import *
# from bot import *
from utils.constants import FINISH_STATE


class FinishState:
    def handle_message(self, msg, bot):
        message = None
        if 'yes' in msg.get_text().lower():
            message = "OK, let's play again, \n Are u ready??"
            bot.set_to_choose_artist_state()

        elif 'no' in msg.get_text().lower():
            message = return_user_message(FINISH_STATE)

        return message

        