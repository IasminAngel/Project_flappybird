# README

## Flappy Bird em Python com Pygame
- Este projeto é uma implementação do jogo Flappy Bird usando Python e a biblioteca Pygame. O objetivo do jogo é controlar um pássaro para evitar obstáculos (canos) e ganhar pontos passando por eles.

## Requisitos

- Python: Certifique-se de ter Python 3.x instalado.
- Pygame: Você pode instalar o Pygame usando o seguinte comando:

```
pip install pygame
```

## Estrutura do Projeto

imgs/: Pasta contendo as imagens usadas no jogo.

pipe.png: Imagem dos canos.

base.png: Imagem do chão.

bg.png: Imagem do fundo.

bird1.png, bird2.png, bird3.png: Imagens do pássaro em diferentes posições.

main.py: Arquivo principal do jogo que contém a lógica e a execução do jogo.

## Execução
- Para executar o jogo, você deve ter a estrutura de pastas e imagens conforme descrito. Navegue até o diretório onde o arquivo main.py está localizado e execute:

```
python main.py
```


## Controles

Espaço: Pular (faz o pássaro subir)

## Funcionamento

Tela Inicial: O jogo começa automaticamente com o pássaro caindo e os canos se movendo.

Objetivo: Evite os canos e tente acumular o maior número de pontos possível.

Game Over: Quando o pássaro colide com um cano ou o chão, a tela de Game Over será exibida, e você poderá escolher se deseja continuar ou sair do jogo.

## Código

- Aqui está uma visão geral das principais classes e funções:

Classe Passaro: Gerencia o pássaro, incluindo movimento, animação e rotação.

Classe Cano: Gerencia os canos, incluindo posicionamento, movimento e colisão.

Classe Chao: Gerencia o chão em movimento.

Função desenha_tela(): Desenha o fundo, pássaros, canos, e pontuação na tela.

Função tela_game_over(): Exibe a tela de Game Over e permite ao usuário continuar ou sair do jogo.

Função main(): Função principal que inicializa o jogo, gerencia eventos e atualiza a tela, como exemplo, a tela de Game Over.

## Contribuições

- Se você deseja contribuir para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

- Este projeto é fornecido "como está" sem garantias de qualquer tipo. Veja o LICENSE para mais detalhes.

- Se você encontrar problemas ou tiver dúvidas, por favor, entre em contato ou abra uma issue no repositório do GitHub. Divirta-se jogando! 🎮

- Nota: Certifique-se de substituir o link do repositório no README com o link real do seu projeto no GitHub.
