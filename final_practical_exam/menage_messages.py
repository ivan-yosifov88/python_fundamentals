def add_user(mail_box, user, sender, receiver):
    if user not in mail_box:
        mail_box[user] = {'send': sender, 'received': receiver}
    return mail_box


def user_in_mail_box(mail_box, user):
    if user in mail_box:
        return True
    return False


def message_command(mail_box, message_sender, message_receiver, MAXIMUM_MESSAGES_CAPACITY):
    if user_in_mail_box(mail_box, message_sender) and user_in_mail_box(mail_box, message_receiver):
        mail_box[message_sender]['send'] += 1
        all_sender_messages = mail_box[message_sender]['send'] + mail_box[message_sender]['received']
        if all_sender_messages == MAXIMUM_MESSAGES_CAPACITY:
            print(f"{message_sender} reached the capacity!")
            mail_box.pop(message_sender)
        mail_box[message_receiver]['received'] += 1
        all_receiver_messages = mail_box[message_receiver]['received'] + mail_box[message_receiver]['send']
        if all_receiver_messages == MAXIMUM_MESSAGES_CAPACITY:
            print(f"{message_receiver} reached the capacity!")
            mail_box.pop(message_receiver)
    return mail_box


def empty_command(mail_box, command_data):
    if command_data == "All":
        mail_box.clear()
    else:
        user = command_data
        if user_in_mail_box(mail_box, user):
            mail_box.pop(user)
    return mail_box


MAXIMUM_MESSAGES_CAPACITY = int(input())

data = input()

message_box = {}

while not data == "Statistics":
    command_info = data.split("=")
    command = command_info[0]
    if command == "Add":
        username = command_info[1]
        send = int(command_info[2])
        received = int(command_info[3])
        add_user(message_box, username, send, received)
    elif command == "Message":
        sender = command_info[1]
        receiver = command_info[2]
        message_command(message_box, sender, receiver, MAXIMUM_MESSAGES_CAPACITY)
    elif command == "Empty":
        data = command_info[1]
        empty_command(message_box, data)
    data = input()

print(f"Users count: {len(message_box)}")

if message_box:
    sorted_message_box = sorted(message_box.items(), key=lambda x:(-x[1]['received'], x[0]))
    for user, messages in sorted_message_box:
        all_messages_of_current_user = messages['send'] + messages['received']
        print(f"{user} - {all_messages_of_current_user}")

