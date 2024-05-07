# um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares
lista_num = []
lista_imp = []

while True:
  try:
    num = int(input('Enter a number (enter a letter when you want to close): '))
    lista_num.append(num)
    if num % 2 == 1:
      lista_imp.append(num)
  except ValueError:
    break
  
print('The sum of the odd numbers entered is:', sum(lista_imp))