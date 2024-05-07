# um programa que leia uma lista de números do usuário e exiba a média desses números
num = int(input('How many numbers do you want to receive? '))

lista = []

for c in range(num):
  n = int(input('Enter the {}º number: '.format(c + 1)))
  lista.append(n)
  media = int(sum(lista)/num)

print('The average of the numbers entered is:', media)