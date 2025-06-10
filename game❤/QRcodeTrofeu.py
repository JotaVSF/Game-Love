import qrcode
import os

caminho = os.path.join(os.getcwd(), "qr_code_youtube.png")
dado = 'https://www.youtube.com/watch?v=6EEW-9NDM5k'
img = qrcode.make(dado)
img.save(caminho)
print(f"QR Code salvo em: {caminho}")