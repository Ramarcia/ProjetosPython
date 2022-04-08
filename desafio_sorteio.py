
#joguinho de adivnhação

from random import randint
computador =( randint(0,10))# faz o computador fazer o sorteio de um numero aleatorio

jogador =int(input("Vou pensar em um numero, tente adivinha! "))# jogador tenta advinhar.
if jogador == computador:
    print("Parabens voce venceu!")
else:
    print("Voce FAlhou, o numero que eu pensei foi {} e nao no numero6 {}".format(computador,jogador))

