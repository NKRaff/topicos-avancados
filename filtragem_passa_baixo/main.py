import cv2
import numpy as np
from filtragem import Filtragem

imagem = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
novaImagem = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
dimensoesImagem = imagem.shape
mascara = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
]

# Filtragem Manual
filtragem = Filtragem(imagem, mascara)

for i in range(dimensoesImagem[0]):
  for j in range(dimensoesImagem[1]):
    novaImagem[i, j] = filtragem.convolucao([i, j])

cv2.imwrite('imagem_filtrada_manual.png', novaImagem)

# Filtragem OpenCV
kernel = np.ones((7, 7), np.float32) / 49
imagemOpenCV = cv2.filter2D(imagem, -1, kernel)
cv2.imwrite('imagem_filtrada_opencv.png', imagemOpenCV)