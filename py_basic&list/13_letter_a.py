# um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a"
qt = int(input('Enter the number of words you will type: '))

lista = []
comeca_a = False

for i in range(qt):
  palavra = str(input('Enter the {}° word: '.format(i+1)))
  lista.append(palavra)

if(comeca_a):
  print('The words entered starting with the letter "A" are: ')
  for palavra in lista:
    if palavra.lower().startswith('a'):
      print(palavra)
else:
    print("No word begins with the letter 'a'.")