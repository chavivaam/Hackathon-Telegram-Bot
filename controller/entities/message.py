class Message:
    def __init__(self, req_as_json):
        self.text = req_as_json['message']['text']
        self.chat_id = req_as_json['message']['chat']['id']

    def get_text(self):
        return self.text
    
    def get_chat_id(self):
        return self.chat_id