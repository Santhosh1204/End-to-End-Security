from django.shortcuts import render
from cryptography.fernet import Fernet

# Create your views here.


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
   
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    dm = decrypted_message.decode()
    return dm
generate_key()

def home(request):
    m = ""
    m = request.GET.get('mess')
    if m is None:
        m = "sample text"
    en_mess = encrypt_message(m)
    de_mess = decrypt_message(en_mess)
    return render(request,'home.html',{'e':en_mess, 'd':de_mess})
