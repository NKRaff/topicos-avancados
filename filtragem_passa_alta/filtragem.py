import numpy as np

class Filtragem:
  def __init__(self):
    pass

  def convolucao(self, imagem, mascara, dimensao, tipo):
    deslocamento_x = len(mascara) // 2
    deslocamento_y = len(mascara[0]) // 2
    matriz = np.zeros((dimensao[0], dimensao[1]))

    for img_x in range(dimensao[0]):
      for img_y in range(dimensao[1]):
        soma = 0
        contador = 0
        mascaraLinha = 0
        mascaraColuna = 0

        for mascara_x in range(-deslocamento_x, deslocamento_x+1):
          for mascara_y in range(-deslocamento_y, deslocamento_y+1):

            x = img_x + mascara_x
            y = img_y + mascara_y

            if x < 0 or x >= dimensao[0]:
              x = img_x + (mascara_x * -1)

            if y < 0 or y >= dimensao[1]:
              y = img_y + (mascara_y * -1)

            soma += mascara[mascaraLinha][mascaraColuna] * float(imagem[x, y])
            contador += 1
            mascaraColuna += 1

          mascaraColuna = 0
          mascaraLinha += 1

        matriz[img_x, img_y] = soma / contador if tipo == "baixa" else soma
        
    return matriz
            