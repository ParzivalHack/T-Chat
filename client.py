import socket, threading, os
os.system("toilet T-Chat")
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect(('127.0.0.1', 7976))                             #connecting client to server

def receive():
    while True:                                                 #making valid connection
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:                                                 #case on wrong ip/port details
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                 #message layout
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   #sending messages 
write_thread.start()
