# TOKEN = '1428832645:AAEn_hDL2vKF1Fk6BfaD8SOIvbFivTMTpQI'
# TOKEN = '1476403386:AAFJt-jgImdOIM_f4WNlnV-GFmJL5hIlEeg'
TOKEN = '1490629303:AAFVSXtMy6XEt25yHLSFAH6TzkgjU3nwjg0'
NGROK_URL = 'https://f2a126d479c1.ngrok.io'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/message'.format(NGROK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
FFMPEG_URL = r"C:\ffmpeg\bin\ffmpeg.exe"
AUDIO_FILE_NAME = "SonGuess.mp3"
API_KEY = "AIzaSyD-yadZ-B8-QDbdbRiMpoAdSjk8Iy1vkIs"
BASE_YOUTUBE_API_URL="https://www.googleapis.com/youtube/v3/"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "music_challenger"
