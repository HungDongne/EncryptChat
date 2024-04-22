import os
import rsa

def generate_key():
    public_key, private_key = rsa.newkeys(1024)
    save_key(public_key, "public.pem")
    save_key(private_key, "private.pem")
    return public_key, private_key

def save_key(key, filename):
    with open(filename, "wb") as file:
        file.write(key.save_pkcs1())

def get_public_key():
    try:
        with open("public.pem", "rb") as file:
            key_data = file.read()
        return rsa.PublicKey.load_pkcs1(key_data)
    except Exception as e:
        return None

def get_private_key():
    try:
        with open("private.pem", "rb") as file:
            key_data = file.read()
        return rsa.PrivateKey.load_pkcs1(key_data)
    except Exception as e:
        return None

def convert_bytes_to_public_key(key_bytes):
    return rsa.PublicKey.load_pkcs1(key_bytes)

def convert_bytes_to_private_key(key_bytes):
    return rsa.PrivateKey.load_pkcs1(key_bytes)

def convert_public_key_to_bytes(key):
    return key.save_pkcs1()

def convert_private_key_to_bytes(key):
    return key.save_pkcs1()
