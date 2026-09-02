class Filtragem:
  def __init__(self, imagem, mascara):
    self.imagem = imagem
    self.mascara = mascara
    self.distancia = int(len(self.mascara) / 2)
    self.dimensoes = self.imagem.shape

  def convolucao(self, posicao):
    soma = 0
    mascaraLinha = 0
    mascaraColuna = 0

    for i in range(-self.distancia, self.distancia+1):
      for j in range(-self.distancia, self.distancia+1):
        x = posicao[0] + i
        y = posicao[1] + j

        if 0 <= x < self.dimensoes[0] and 0 <= y < self.dimensoes[1]:
          soma += self.mascara[mascaraLinha][mascaraColuna] * int(self.imagem[x, y])

        else:
          if x < 0 or x >= self.dimensoes[0]:
            i = i * -1

          if y < 0 or y >= self.dimensoes[1]:
            j = j * -1

          x = posicao[0] + i 
          y = posicao[1] + j

          soma += self.mascara[mascaraLinha][mascaraColuna] * int(self.imagem[x, y])

        mascaraColuna += 1

      mascaraColuna = 0
      mascaraLinha += 1

    novaCor = int(soma / (len(self.mascara) ** 2))

    return novaCor