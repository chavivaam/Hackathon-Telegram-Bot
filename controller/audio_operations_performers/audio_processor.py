from pydub import AudioSegment
from utils.config import *
from utils.constants import FILE_LOCATION, GlobalNum


def split_audio_file(path, miliseconds):

    AudioSegment.converter = FFMPEG_URL

    sound = AudioSegment.from_file(path)

    first_half = sound[:miliseconds]

    # create a new file
    first_half.export(FILE_LOCATION + str(GlobalNum.file_name_counter) + AUDIO_FILE_NAME, format="mp3")

    GlobalNum.file_name_counter = GlobalNum.file_name_counter + 1
