# um programa que leia um número do usuário e determine se esse número é par ou ímpar
num = int(input('Enter the number: '))

if num % 2 == 0:
  print('The number', num, 'is EVEN!')
else:
  print('The number', num, 'is ODD!')