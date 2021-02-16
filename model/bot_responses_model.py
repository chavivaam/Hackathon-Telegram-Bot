import pymysql
import random
from utils.config import *

connection = pymysql.connect(
    host="localhost",
    user=DB_USER,
    password=DB_PASSWORD,
    db=DB_NAME,
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def get_message_by_state(state_id, sub_state_id = 0):
    with connection.cursor() as cursor:
        query = "SELECT * FROM Messages WHERE state={} AND sub_state={}".format(state_id,sub_state_id)
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def return_user_message(state_id, sub_state_id=0):
    messages = get_message_by_state(state_id,sub_state_id)
    if sub_state_id == 0:
        return messages[0]['message']
    else:
        random_number = random.randint(0, len(messages)-1)

        return messages[random_number]['message']
        
