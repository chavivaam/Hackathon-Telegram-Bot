import requests
from model.bot_responses_model import return_user_message
from controller.audio_operations_performers.audio_processor import split_audio_file
from utils.constants import PEEK_DURATION, FINISH_STATE, HELP_STATE, FILE_EXTENSION, FILE_LOCATION
from controller.states.choose_artist_state import send_audio
from controller.states.guess_state import GuessState
from utils.config import BASE_TELEGRAM_URL
from controller.states.finish_state import FinishState


class HelpState:
    PEEK_DURATION_HELP = PEEK_DURATION
    
    def handle_message(self, msg, bot):
        res = None
        if 'hint' in msg.get_text().lower():
            HelpState.PEEK_DURATION_HELP += PEEK_DURATION
            split_audio_file(bot.current_file_path, HelpState.PEEK_DURATION_HELP)
            send_audio(msg.chat_id)
            res = "You got an amazing second chance here \n, go ahead and guess again!"
            bot.handle_state(GuessState(msg.get_text(), bot.item_no, "UCVOwOs8Cn4Uv0Hc2foG9YCQ"))

        elif 'answer' in msg.get_text().lower():
            res = return_user_message(FINISH_STATE)
            answer = bot.current_file_path.strip(FILE_EXTENSION + FILE_LOCATION)
            response = requests.get("{}/sendMessage?chat_id={}&text={}"
                       .format(BASE_TELEGRAM_URL, msg.get_chat_id(), answer))
            
            bot.handle_state(FinishState())


        return res      

    def display_menu(self):
        res = return_user_message(HELP_STATE)
        return res