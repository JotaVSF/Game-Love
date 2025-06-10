import qrcode

# Link para o arquivo HTML do jogo (salve como "jogo.html" na mesma pasta)
url_jogo = "http://127.0.0.1:5500/game%E2%9D%A4/game.html" 
img_jogo = qrcode.make(url_jogo)
img_jogo.save("qr_code_jogo.png")
print("QR Code do jogo gerado como 'qr_code_jogo.png'")