# um programa que leia uma lista de números do usuário e exiba o menor número dessa lista
num = int(input('How many numbers do you want to receive? '))

lista = []

for c in range(num):
  n = int(input('Enter the {}º number: '.format(c + 1)))
  lista.append(n)
  menor_numero = min(lista)

print('The largest number entered was: ', menor_numero)