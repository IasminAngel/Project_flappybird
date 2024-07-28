# -- Importação das bibliotecas --

import tkinter as tk
from tkinter import messagebox
import pygame
import random
import os

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
tela_largura = 500
tela_altura = 800

# Carregar imagens
imagem_cano = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
imagem_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
imagem_background = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
imagem_passaro = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

# Inicializando fonte de pontos
pygame.font.init()
fonte_pontos = pygame.font.SysFont('Times New Roman', 45)
fonte_game_over = pygame.font.SysFont('Times New Roman', 100)

# Classe do pássaro
class Passaro:
    rotacao_maxima = 25
    velocidade_rotacao = 20
    tempo_animacao = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = imagem_passaro[0]

    def pular(self):
        self.velocidade = -9.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        if deslocamento > 10:
            deslocamento = 10
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.rotacao_maxima:
                self.angulo = self.rotacao_maxima
        else:
            if self.angulo > -90:
                self.angulo -= self.velocidade_rotacao

    def desenhar(self, tela):
        self.contagem_imagem += 1

        if self.contagem_imagem < self.tempo_animacao:
            self.imagem = imagem_passaro[0]
        elif self.contagem_imagem < self.tempo_animacao * 2:
            self.imagem = imagem_passaro[1]
        elif self.contagem_imagem < self.tempo_animacao * 3:
            self.imagem = imagem_passaro[2]
        elif self.contagem_imagem < self.tempo_animacao * 4:
            self.imagem = imagem_passaro[1]
        elif self.contagem_imagem >= self.tempo_animacao * 4 + 1:
            self.imagem = imagem_passaro[0]
            self.contagem_imagem = 0

        if self.angulo <= -80:
            self.imagem = imagem_passaro[1]
            self.contagem_imagem = self.tempo_animacao * 2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

# Classe do cano
class Cano:
    distancia = 200
    velocidade = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.cano_topo = pygame.transform.flip(imagem_cano, False, True)
        self.cano_base = imagem_cano
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.cano_topo.get_height()
        self.pos_base = self.altura + self.distancia

    def mover(self):
        self.x -= self.velocidade

    def desenhar(self, tela):
        tela.blit(self.cano_topo, (self.x, self.pos_topo))
        tela.blit(self.cano_base, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.cano_topo)
        base_mask = pygame.mask.from_surface(self.cano_base)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        return base_ponto or topo_ponto

# Classe do chão
class Chao:
    velocidade = 5
    largura = imagem_chao.get_width()
    imagem = imagem_chao

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.largura

    def mover(self):
        self.x1 -= self.velocidade
        self.x2 -= self.velocidade

        if self.x1 + self.largura < 0:
            self.x1 = self.x2 + self.largura
        if self.x2 + self.largura < 0:
            self.x2 = self.x1 + self.largura

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x1, self.y))
        tela.blit(self.imagem, (self.x2, self.y))

# Função para desenhar a tela
def desenha_tela(tela, passaros, canos, chao, pontos):
    tela.blit(imagem_background, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = fonte_pontos.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (tela_largura - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()

# Função de tela de game over
def tela_game_over(tela, chao):
    game_over_text = fonte_game_over.render("Game Over", 1, (255, 255, 255))
    tela.blit(game_over_text, (tela_largura // 2 - game_over_text.get_width() // 2, tela_altura // 2 - game_over_text.get_height() // 2))
    chao.desenhar(tela)
    pygame.display.update()
    pygame.time.wait(1000)
  
  
    resposta = messagebox.askquestion("Game Over", "Você deseja continuar?")

    if resposta == 'yes':     
        if __name__ == '__main__':
         main()
    else:
        pygame.time.wait(1000)
        pygame.quit()
        quit()

# Função principal
def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((tela_largura, tela_altura))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    rodando = False
                    tela_game_over(tela, chao)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()
            if cano.x + cano.cano_topo.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                rodando = False
                tela_game_over(tela, chao)

        desenha_tela(tela, passaros, canos, chao, pontos)

if __name__ == '__main__':
    main()