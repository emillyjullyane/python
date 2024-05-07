# um programa que leia uma lista de números do usuário e exiba a soma desses números
num = int(input('How many numbers do you want to receive? '))
sum = 0

for c in range(num):
  n = int(input('Enter the {}º number: '.format(c + 1)))
  sum += n

print('The sum of the numbers entered is: ', sum)
