import qrcode
from PIL import Image
import qrcode.constants

text=input("write your text hear:")
qr=qrcode.QRCode(version=1,error_correction = qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data(text)
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color = "black")
img.save("new_qr.png")

