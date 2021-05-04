from covidsafecore import generateqrcode
from PIL import Image
from pyzbar import pyzbar


GENERATED_DIRECTORY = "generated/"

num = input("[+ Dichill +] Input QR NAME: ")

scanned = num + ".png"
scanned = Image.open(GENERATED_DIRECTORY + scanned)
scanned = pyzbar.decode(scanned)
scanned = scanned[0].data

print("Info: " + generateqrcode.DecryptInfo(scanned,
                                            "rsknqzk_qL2MBi1GEbgwl9AXaI4XLuosm30ZrHDyqD0=").decode())
