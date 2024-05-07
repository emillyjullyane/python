# um programa que leia uma lista de números do usuário e exiba somente os números pares
lista_pares = []
lista_num = []

while True:
    try:
        num = input('Enter a number: (Enter a letter when you want to stop!): ')
        lista_num.append(int(num))
        if num.isdigit():
          num = int(num)
          if int(num) % 2 == 0:
              lista_pares.append(num)
    except ValueError:
        break

# print('All numbers entered:', lista_num)
print('Even numbers typed:', lista_pares)