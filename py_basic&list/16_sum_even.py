# um programa que leia uma lista de números do usuário e exiba a soma dos números pares
lista_num = []
lista_pares = []

while True:
  try:
    num = int(input('Enter a number (enter a letter when you want to close): '))
    lista_num.append(num)
    if num % 2 == 0:
      lista_pares.append(num)
  except ValueError:
    break
  
print('The sum of the even numbers entered is: ', sum(lista_pares))