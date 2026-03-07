import qrcode
import os
from PIL import Image
#Encoding data
data = "https://github.com/mrx8266/make_qr_from_link"
folder = "images" 

os.makedirs('images', exist_ok=True)

#QR code generation
img = qrcode.make(data)

#img saving
img.save('images/new_image.png')
