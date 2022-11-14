from chatroom.model.message_model import MessageModel

def get_sample_message_list():
    msg1 = MessageModel(user_id='123', user_name='user1', content='hello', room='room1')
    msg2 = MessageModel(user_id='124', user_name='tricky', content='hey, how you doin', room='room1')
    msg3 = MessageModel(user_id='125', user_name='johnny', content='I am fine, thanks', room='room1')
    msg4 = MessageModel(user_id='126', user_name='livvy', content='DADDY!', room='room1')
    msg5 = MessageModel(user_id='127', user_name='charlie_mae', content='I am hungry', room='room1')
    msg6 = MessageModel(user_id='124', user_name='tricky', content='Everybody be quiet', room='room1')
    msg7 = MessageModel(user_id='127', user_name='charlie_mae', content='WAH!', room='room1')
    message_list = [msg1, msg2, msg3, msg4, msg5, msg6, msg7]

    return message_list