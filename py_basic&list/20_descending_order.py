# um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente
numeros = input('Enter a space-separated list of numbers: ').split()

lista_num = []

for num in numeros:
  num = float(num)
  lista_num.append(num)
  
lista_num.sort()

lista_num.reverse()

print('Numbers in descending order: ', lista_num)