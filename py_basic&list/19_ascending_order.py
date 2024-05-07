# um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem crescente
numeros = input('Enter a space-separated list of numbers: ').split()

lista_num = []

for num in numeros:
  num = float(num)
  lista_num.append(num)
  
lista_num.sort()

print('Numbers in ascending order: ', lista_num)