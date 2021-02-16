import requests
from model.bot_responses_model import *
from controller.states.guess_state import GuessState
from controller.audio_operations_performers import audio_downloader, you_tube_searcher, audio_processor
from utils.config import NGROK_URL, AUDIO_FILE_NAME, BASE_TELEGRAM_URL
from utils.constants import FILE_LOCATION, FILE_EXTENSION, PEEK_DURATION, GlobalNum


class ChooseArtistState:

    def handle_message(self, msg, bot):
        # get the audio file by calling the modulrs responsible for that
        # should get 2 params : audio_id, item_no
        audio_id, item_no = you_tube_searcher.search_audio_by_artist(msg.get_text()) 
        video_title = audio_downloader.download_webm_file_by_id(audio_id)
        file_path = FILE_LOCATION  + video_title + FILE_EXTENSION
        audio_processor.split_audio_file(file_path, PEEK_DURATION)

        bot.set_current_file_path(file_path)
        bot.set_item_no(item_no)
        send_audio(msg.chat_id)

        bot.handle_state(GuessState(msg.get_text(), item_no, "UCVOwOs8Cn4Uv0Hc2foG9YCQ"))
        return "Go ahead and guess!"
    
def send_audio(chat_id):

    mp3URL = NGROK_URL + '/' + str(GlobalNum.file_name_counter-1) + AUDIO_FILE_NAME
    URL =  BASE_TELEGRAM_URL + '/sendAudio?chat_id=' + str(chat_id)+'&audio=' + mp3URL
    get_res = requests.get(URL)

