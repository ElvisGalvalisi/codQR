import os
import pyqrcode
from PIL import Image


class QR_Gen(object):
    def __init__(self, text):
        self.qr_image = self.qr_generator(text)

    @staticmethod
    def qr_generator(text):
        qr_code = pyqrcode.create(text)
        file_name = "QR Result"
        save_path = os.path.join(os.path.expanduser('~'), 'Desktop')

        name = f'{save_path}{file_name}.png'
        qr_code.png(name, scale=10)
        image = Image.open(name)
        image = image.resize((200,200), Image.ANTIALIAS)
        image.show()

if __name__ == "__main__":
    QR_Gen(input("[QR] Ingresar texto para codificar: "))