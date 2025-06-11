import qrcode

# Link para o arquivo HTML do jogo (salve como "jogo.html" na mesma pasta)
url_jogo = "https://game-love-alpha.vercel.app/" 
img_jogo = qrcode.make(url_jogo)
img_jogo.save("qr_code_jogo.png")
print("QR Code do jogo gerado como 'qr_code_jogo.png'")
