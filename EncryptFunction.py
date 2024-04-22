from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import os
import rsa
def encrypt_message(message, public_key):
    try:
        # Chuyển đổi văn bản thành dạng byte
        message = message.encode()

        # Mã hóa văn bản sử dụng khóa công khai
        ciphertext = rsa.encrypt(message, public_key)
        return ciphertext
    except Exception as e:
        print("Error occurred during encryption:", e)
        return None

def decrypt_message(ciphertext, private_key):
    try:
        # Giải mã văn bản sử dụng khóa riêng tư
        plaintext = rsa.decrypt(ciphertext, private_key)

        # Chuyển đổi văn bản từ dạng byte thành chuỗi
        plaintext = plaintext.decode()

        return plaintext
    except Exception as e:
        print("Error occurred during decryption:", e)
        return None
