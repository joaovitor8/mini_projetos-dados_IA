import cv2
import numpy as np
import pickle
from imutils import paths
from keras.api.models import load_model
from helpers import resize_to_fit
from tratar_captcha import tratar_imagem

# 4 - Colocando o modelo / IA para resolver os captcha

def quebrar_captcha():
  with open("rotulos_modelo.abc", "+rb") as arquivo_tradutor:
    lb = pickle.load(arquivo_tradutor)

    modelo = load_model("modelo_treinar.hdf5")

    tratar_imagem("resolver", pasta_destino="resolver")

    arquivos = list(paths.list_images("resolver"))


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

      regiao_letras = sorted(regiao_letras, key=lambda lista: lista[0])

      # Desenhar os contornos e separar as letras em arquivos individuais
      imagem_final = cv2.merge([imagem] * 3)
      previsao = []

      for retangulo in regiao_letras:
        x, y, largura, altura = retangulo
        imagem_letra = imagem[y-2:y+altura+2, x-2:x+largura+2]

        imagem_letra = resize_to_fit(imagem_letra, 20, 20)

        imagem_letra = np.expand_dims(imagem_letra, axis=2)
        imagem_letra = np.expand_dims(imagem_letra, axis=0)

        letra_prevista = modelo.predict(imagem_letra)
        letra_prevista = lb.inverser.transfom(letra_prevista)[0]
        previsao.append(letra_prevista)

        ponto_inicial = (x-2, y-2)
        ponto_final = (x+largura+2, y+altura+2)

        cv2.rectangle(imagem_final, ponto_inicial, ponto_final, (0, 255, 0), 1)
      
      texto_previsao = "".join(previsao)

      print(texto_previsao)
      return texto_previsao



if __name__ == "__name__":
  quebrar_captcha
