import socket
import KeyFunction
import EncryptFunction

IP = "192.168.0.103"
PORT = 8000

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.connect((IP, PORT))

PUBLIC_KEY = KeyFunction.get_public_key()

while True:
    message = input("->")
    if message == "exit":
        break
    sever.send(EncryptFunction.encrypt_message(message, PUBLIC_KEY))
    print("Message sent")

sever.close()