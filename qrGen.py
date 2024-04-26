import pyqrcode
import png
from pyqrcode import QRCode
QRString = input("Ingrese texto: ")
url = pyqrcode.create(QRString)
nomQR = input("Ingrese nombre del archivo QR: ")
url.png(f'C:\codQR\{nomQR}.png', scale= 8)
url.show()