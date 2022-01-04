import os


def send_message(title, message, urgency, time):
    os.system(f'notify-send -u {urgency} -t {time} "{title}" "{message}"')


send_message('This is a multi word title', 'This is a multi word message', 'normal', 250)

# def pingtest(host):
#     os.

# TODO : Find out how to exit running terminals processes from os library