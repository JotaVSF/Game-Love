import qrcode
import os

caminho = os.path.join(os.getcwd(), "qr_code_youtube.png")
dado = 'https://m.youtube.com/shorts/l5jI54nFrko'
img = qrcode.make(dado)
img.save(caminho)
print(f"QR Code salvo em: {caminho}")