from controller.states.start_state import *
from controller.states.help_state import *
from utils import config


class Bot:

    def __init__(self):
        self.game_state = StartState()
        self.current_file_path = ''
        self.item_no = 0

    def handle_state(self, state):
        self.game_state = state

    def handle_message(self, msg):
        res = None
        if self.is_need_help(msg):
            helper = HelpState()
            res = helper.display_menu()
            self.game_state = helper
        else: 
            res = self.game_state.handle_message(msg, self)

        return res

    def set_current_file_path(self, file_path):
        self.current_file_path = file_path

    def set_item_no(self, item_no):
        self.item_no = item_no

    def is_need_help(self, msg):
        if "help" in msg.get_text().lower():
            return True

    def set_to_choose_artist_state(self):
        self.handle_state(ChooseArtistState())        

    

