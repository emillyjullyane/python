# um programa que leia uma lista de números do usuário e exiba o produto desses números
lista_num = []

def mult(lista_num):
    result = 1
    for c in lista_num:
        result *= c
    return result

numeros = input("Enter a space-separated list of numbers: ").split()
for num in numeros:
    lista_num.append(int(num))

resultado = mult(lista_num)
print('Multiplication of numbers: ', resultado)
