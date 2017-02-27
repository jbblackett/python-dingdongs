import os
from time import gmtime, strftime

path = 'chatroom.txt'
chat = []

def update():
    global chat
    chat = []
    with open(path, 'r') as f:
        for line in f:
            chat.append(line)
while not chat:
    update()
for item in chat:
    print(item, end='')
n = chat[-1]

while True:
    update()
    if chat:
        if chat[-1] != n:
            n = chat[-1]
            print(n, end='')
