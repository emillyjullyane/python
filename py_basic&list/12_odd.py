# um programa que leia uma lista de números do usuário e exiba somente os números ímpares
lista_impares = []
lista_num = []

while True:
    try:
        num = input('Enter a number: (Enter a letter when you want to stop!): ')
        lista_num.append(int(num))
        if num.isdigit():
          num = int(num)
          if int(num) % 2 == 1:
              lista_impares.append(num)
    except ValueError:
        break

print('Odd numbers typed:', lista_impares)