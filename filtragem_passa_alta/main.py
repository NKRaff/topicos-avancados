import cv2
import numpy as np
from filtragem import Filtragem
from conversao import Conversao

imagem = cv2.imread("image/imagem_original.png", cv2.IMREAD_GRAYSCALE)
dimensoesImagem = imagem.shape
mascara = [
  [0, 1, 0],
  [1, -4, 1],
  [0, 1, 0]
]

filtragem = Filtragem()
conversao = Conversao()

matriz = filtragem.convolucao(imagem, mascara, dimensoesImagem, "alta")
nova_imagem = conversao.inteiro(conversao.normalizacao(matriz))
cv2.imwrite('image/imagem_filtrada.png', nova_imagem)