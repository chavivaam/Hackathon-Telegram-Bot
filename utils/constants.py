FILE_LOCATION = "Downloads/"
FILE_EXTENSION = ".webm"

PEEK_DURATION = 2000


class GlobalNum:
    file_name_counter = 0


START_STATE = 1
GUESS_STATE = 2
FINISH_STATE = 3
CHOOSE_ARTIST_STATE = 4
HELP_STATE = 5

GOOD_GUESS = 1
BAD_GUESS = 2

WRONG_HELP_TYPE = 1
WRONG_HELP_TYPE_CONS = 2