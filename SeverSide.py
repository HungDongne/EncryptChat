import socket
import KeyFunction
import EncryptFunction

IP = "192.168.0.103"
PORT = 8000

SEVER_ACCOUNT = "narutodjh@gmail.com"
SEVER_PASSWORD = "17112004"

PUBLIC_KEY = KeyFunction.get_public_key()
PRIVATE_KEY = KeyFunction.get_private_key()

# print("Public key: ", PUBLIC_KEY)
# print("Private key: ", PRIVATE_KEY)

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind((IP, PORT))
sever.listen(5)
print("Sever is listening on", IP, ":", PORT)
client, addr = sever.accept()
print("Connected to", addr)

while True:
    message = client.recv(1024)
    print("Message crypted: ", message)
    print("Message decrypted: ", EncryptFunction.decrypt_message(message, PRIVATE_KEY))