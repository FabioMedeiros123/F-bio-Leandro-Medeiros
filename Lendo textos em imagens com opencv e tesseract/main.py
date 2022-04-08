import pytesseract
import cv2

#Lendo a imagem com o opencv
imagem = cv2.imread('bomdia1.jpg')

#Resolvendo problema de instalação do tesseract
#1º - baixar o tesseract (versão 64 bits) disponível no link: https://github.com/UB-Mannheim/tesseract/wiki
#2º - instalar
#3º - copiar o caminho de instalação indicado no momento da instalação e definir no código
caminho = r"C:\Program Files\Tesseract-OCR"

#Passando o caminho para tesseract_cmd
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

#Transformando para texto usando o tesseract
# Baixar outras línguas para usar o português através do link: https://github.com/tesseract-ocr/tessdata
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)