# um programa que leia uma lista de números do usuário e exiba o maior número dessa lista
num = int(input('How many numbers do you want to receive? '))

lista = []

for c in range(num):
  n = int(input('Enter the {}º number: '.format(c + 1)))
  lista.append(n)
  maior_numero = max(lista)

print('The largest number entered was: ', maior_numero)