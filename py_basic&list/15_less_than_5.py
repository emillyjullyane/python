# um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5
qt = int(input('Enter the number of numbers that will be entered: '))

lista_num = []
menor_cinco = []

for c in range(qt):
  num = float(input('Enter the {}° word: '.format(c+1)))
  lista_num.append(num)
  if num < 5:
    menor_cinco.append(num)

print("Less than 5: ", menor_cinco)

if num > 5:
  print('There are no numbers smaller than 5!')