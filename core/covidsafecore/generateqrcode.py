import qrcode
from cryptography.fernet import Fernet
import random
import os

# This is where generated QR Codes are saved.
PATH_TO_DIRECTORY = os.getcwd() + "/core/generated/"
SECRET_KEY = 'rsknqzk_qL2MBi1GEbgwl9AXaI4XLuosm30ZrHDyqD0='

# When generated, if a anonymous user goes to the link of the generated qr, they can't access it
# Unless they have the certain parameter that is needed
# to go to that link.


def randnum():
    return random.randint(1000, 9999)


def EncryptInfo(name, address):
    info = name + "-" + address
    info = info.encode()
    f = Fernet(SECRET_KEY)
    return f.encrypt(info)


def DecryptInfo(data, token):
    f = Fernet(token)
    decrypted_data = f.decrypt(data)
    return decrypted_data


def GenerateQRCode(name, address):
    data = EncryptInfo(name, address)
    img = qrcode.make(data)

    print(data)

    number = randnum()
    print("[DrX] Creating QR CODE")
    img.save(PATH_TO_DIRECTORY + str(number) + ".png")
    return str(number)
