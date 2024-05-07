# um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa
num = int(input('How many worlds do you want to receive? '))

lista = []

for c in range(num):
  world = input('Enter the {}º world: '.format(c + 1))
  lista.append(world)

mais_longa = ""

for palavra in lista:
    if len(palavra) > len(mais_longa):
        mais_longa = palavra

print('The longest word is: ', mais_longa)