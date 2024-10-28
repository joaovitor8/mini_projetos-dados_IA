import cv2
import os
import glob

# 2 - Separando as letras e numeros para treinamento indivdiual

arquivos = glob.glob('captcha_tratado/*')

for arquivo in arquivos:
  imagem = cv2.imread(arquivo)
  imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

  _, nova_imagem = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV)

  # Encontra os contornos de cada letra
  contornos, _ = cv2.findContours(nova_imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  regiao_letras = []

  # Filtrar os contornos que são realmente de letras
  for contorno in contornos:
    (x, y, largura, altura) = cv2.boundingRect(contorno)
    area = cv2.contourArea(contorno)

    if area > 115:
      regiao_letras.append((x, y, largura, altura))
  
  # if len(regiao_letras) != 5:
  #   continue
  
  # Desenhar os contornos e separar as letras em arquivos individuais
  imagem_final = cv2.merge([imagem] * 3)

  i = 0
  for retangulo in regiao_letras:
    x, y, largura, altura = retangulo
    imagem_letra = imagem[y-2:y+altura+2, x-2:x+largura+2]

    ponto_inicial = (x-2, y-2)
    ponto_final = (x+largura+2, y+altura+2)

    i += 1
    nome_arquivo = os.path.basename(arquivo).replace('.png', f"Letra{i}.png")
    cv2.imwrite(f'letras-numeros/{nome_arquivo}', imagem_letra)
    cv2.rectangle(imagem_final, ponto_inicial, ponto_final, (0, 255, 0), 1)
  
  nome_arquivo_original = os.path.basename(arquivo)
  cv2.imwrite(f'identificando_letras-numeros/{nome_arquivo_original}', imagem_final)
