import cv2
import numpy

cores = {
  "azul": [255, 0, 0],
  "verde": [0, 255, 0],
  "vermelho": [0, 0, 255],
  "amarelo": [0, 255, 255]
}

altura_imagem = int(input("Altura da imagem: "))
largura_imagem = int(input("Largura da imagem: "))
coordenada_circulo = list(map(int, input("Coordenadas do centro da circunferência (x,y): ").split(",")))
raio_circulo = int(input("Raio da circunferência: "))
cor = input("Cor desejada (opções: azul, verde, vermelho ou amarelo): ")
cor = cores[cor]

imagem = numpy.zeros((altura_imagem, largura_imagem, 3), numpy.uint8)

for i in range(altura_imagem):
  for j in range(largura_imagem):
    if (i - coordenada_circulo[0]) ** 2 + (j - coordenada_circulo[1]) ** 2 <= raio_circulo ** 2:
      imagem[i][j] = cor

cv2.imshow("imagem", imagem)
cv2.waitKey(0)
