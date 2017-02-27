import os
from time import gmtime, strftime

user = input('Username: ') + ': '
path = 'chatroom.txt'

def sendMessage(msg):
    t = strftime('[%d/%m/%y %H:%M:%S] ', gmtime())
    f = open(path, 'a')
    f.write(t + user + msg + '\n')
    f.close()

while True:
    sendMessage(input('\nWrite a message: '))
