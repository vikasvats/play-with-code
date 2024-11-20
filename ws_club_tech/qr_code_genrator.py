# this is the code to generate qr code
import qrcode
# this is the code to generate the simple qr code

text = input("What do you want to generate:")

imag = qrcode.make(text)
imag.save("vikas.png")
