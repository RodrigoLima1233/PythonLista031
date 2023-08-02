'''
9) Fazer um algorítimo que pergunte 1 número e apresente:

a) O próprio número
b) O quadrado deste número
c) A raíz quadrada deste número
'''

import math

num = float(input("Adicione um número:"))

num1 = num
num2 = math.pow(num,2)
num3 = math.sqrt(num)

print("O número:",num)
print("O quadrado dele é:", num2)
print("Sua raiz quadrada é:", num3)


