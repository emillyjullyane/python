# um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10
qt = int(input('Enter the number of numbers that will be entered: '))

lista_num = []
maior_dez = []

for c in range(qt):
  num = float(input('Enter the {}° word: '.format(c+1)))
  lista_num.append(num)
  if num > 10:
    maior_dez.append(num)

print("Greater than 10: ", maior_dez)

if num < 10:
  print('There are no numbers greater than 10!')
