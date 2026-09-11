import numpy as np

class Conversao:
  def __init__(self):
    pass

  def absoluto(self, matriz):
    nova_matriz = np.zeros((len(matriz), len(matriz[0])))
    for i in range(len(matriz)):
      for j in range(len(matriz[0])):
        nova_matriz[i][j] = abs(matriz[i][j])
    return nova_matriz

  def normalizacao(self, matriz):
    nova_matriz = np.zeros((len(matriz), len(matriz[0])))
    min = matriz[0][0]
    max = matriz[0][0]

    for i in range(len(matriz)):
      for j in range(len(matriz[0])):
        if matriz[i][j] > max:
          max = matriz[i][j]
        if matriz[i][j] < min:
          min = matriz[i][j]

    for i in range(len(matriz)):
      for j in range(len(matriz[0])):
        nova_matriz[i][j] = ((matriz[i][j] - min) / (max - min)) * 255

    return nova_matriz

  def inteiro(self, matriz):
    nova_matriz = np.zeros((len(matriz), len(matriz[0])), np.uint8)
    for i in range(len(matriz)):
      for j in range(len(matriz[0])):
        nova_matriz[i][j] = int(matriz[i][j])
    return nova_matriz