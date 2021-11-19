import random
n1 = str(input'Primeiro número: ')
n2 = str(input'Segundo número: ')
n3 = str(input'Terceiro número: ')
n4 = str(input'Quarto número: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O número sorteado foi {}'.format(escolhido))
