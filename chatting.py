#Chatting with RSA Encryption 

from http import server
import socket
import threading
import rsa

public_key, private_key = rsa.newkeys(1024)
public_keyPartner = None

choice = input("Do you wnat to host(1) or to connect (2):")

if choice =="1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.8.101", 9999))
    server.listen()
    

    client, _=server.accept()

elif choice =="2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.8.101", 9999))

else:
    exit()


def sending_messages(c):
    while True:
        message = input("")
        #Encrypting message using RSA
        c.send(rsa.encrypt(message.encode(), public_keyPartner))
        print("You:" + message)

def receiving_messages(c):
    while True:
        #Decrypting message with RSA
        print("Partner:"+ rsa.decrypt(c.recv(1024), private_key).decode())


threading.Thread(target=sending_messages, args=(client, )).start()
threading.Thread(target=receiving_messages, args=(client, )).start()