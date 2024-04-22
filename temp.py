import os
import rsa
import EncryptFunction
import KeyFunction

private_key = KeyFunction.get_private_key()
if (private_key == None):
    print("Error: Private key is None")
    print("Creating private key ...")
    public_key, private_key = KeyFunction.generate_key()
    print("Private key created")
else:
    print("Private key exists")
    public_key = KeyFunction.get_public_key()
    

# print("Public key: ", public_key)

message = "Hello World"
print("Original message: ", message)
encrypted_message = EncryptFunction.encrypt_message(message, public_key)
print("Encrypted message: ", encrypted_message)
decrypted_message = EncryptFunction.decrypt_message(encrypted_message, private_key)
print("Decrypted message: ", decrypted_message)