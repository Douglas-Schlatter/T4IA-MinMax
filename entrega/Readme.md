# Trabalho 4 de IA - Busca com adversários

## Integrantes do Grupo:

- **Douglas Ardenghi Schlatter** - Cartão: 00332849 - Turma A - 🦧
- **João Paulo Vasquez Dias** - Cartão: 00333827 - Turma A - 🙉
- **Matheus Rodrigues Fonseca** - Cartão: 00332800 - Turma A - 🦍


# Avaliação Tic-Tac-Toe Misere:
**(i) O minimax sempre ganha do randomplayer?**

  Como player 2 o minimax quase sempre ganha do randomplayer, entretando, quando com o papel de player 1, ocorrem alguns empates.

**(ii) O minimax sempre empata consigo mesmo?**

  De acordo com nosso espaço amostral, sim.
  
**(iii) O minimax sempre empata contra as jogadas perfeitas recomendadas pelo
https://nyc.cs.berkeley.edu/uni/games/ttt/variants/misere ? Para verificar isso, use o
humanplayer. No link, faça as jogadas do minimax, e no servidor do kit, faça as
jogadas recomendadas (amarelo ou verde) do link.**

  Sim, ele sempre empata.

# Avaliação Othello:
**(i) Represente em uma matriz de 3 X 3 onde as linhas representam o jogador que inicia
(player 1) e as colunas representam o player 2 e em cada célula, indique se a partida
resultou em vitória (1), derrota (-1) ou empate (0) entre os agentes com cada uma das
heurísticas.**

|Player 1 x Player 2| Heuristica_count       | Heuristica_Mask   | Heuristica_custom  |
|---------------|------------|-----------|---------|
| Heuristica_count| -1   |  -1     |-1|
| Heuristica_Mask| 1    | -1    |-1|
| Heuristica_custom|  -1 |-1 | -1 |


**(ii) Observe e relate qual implementação foi a mais bem-sucedida.**

A implementação mais bem sucedida foi a do mask, sendo a unica 
que conseguiu ganhar uma partida jogando primeiro.


**(iii) Reflita sobre o que pode ter tornado cada heurística melhor ou pior, em termos de
performance.**


Ao jogar Othello, é possível notar como o jogo pode apresentar grandes variações. Ou seja, é possível estar ganhando por uma grande quantidade de peças, mas com uma boa jogada do adversário, pode-se perder toda a vantagem. Dessa forma, concluímos que a heurística que leva em conta a quantidade de peças é inferior à posicional, pois é possível mudar uma grande quantidade de peças de cor ao garantir que os cantos sejam da sua cor. Com isso em mente, a heurística de posicionamento, que leva em conta o posicionamento das peças, torna-se superior à heurística de contagem de peças. Nossa heurística personalizada buscava levar em conta ambas as heurísticas e, embora tenha perdido para a heurística de posicionamento, perdeu por menos pontos de diferença do que a heurística de contagem de peças.Ao jogar Othello, é possível notar como o jogo pode apresentar grandes variações. Ou seja, é possível estar ganhando por uma grande quantidade de peças, mas com uma boa jogada do adversário, pode-se perder toda a vantagem. Dessa forma, concluímos que a heurística que leva em conta a quantidade de peças é inferior à posicional, pois é possível mudar uma grande quantidade de peças de cor ao garantir que os cantos sejam da sua cor. Com isso em mente, a heurística de posicionamento, que leva em conta o posicionamento das peças, torna-se superior à heurística de contagem de peças. Nossa heurística personalizada buscava levar em conta ambas as heurísticas e, embora tenha perdido para a heurística de posicionamento, perdeu por menos pontos de diferença do que a heurística de contagem de peças.


# Feedback 📝
- **Quão fácil ou difícil foi realizar o trabalho?** 😓

  Durante o desenvolvimento do trabalho, enfrentamos um bug específico 🐛, no qual gastamos um bom tempo tentando resolver, 
  mas foi tranquilo 🍃.

- **Utilizaram o auxílio da IA para o desenvolvimento do trabalho?** 💻

  Foi utilizado o IA Copilot 🤖 em algumas funções para autocomplete, no entanto, a IA não foi usada para grandes partes do trabalho. 

- **Como foi trabalhar com o auxílio da IA?** 🤔

  Bom, mas nem tanto 😐.

- **Quais sugestões teria para melhorar o trabalho?** 🛠️
  
  Encontramos problemas no momento de debugar nossas IAs pela falta de UI demonstrando seu comportamento 🖥️, alem disso, e não buscando te criticar 😞 o link para conferir as jogadas perfeitas do tic tac toe Misere estava errado 🚫.
