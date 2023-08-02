'''
Fazer um algarismo que efetue o cálculo do valor de uma prestação em atraso utilizando a fórmula
prestação = valor + (valor x (taxa : 100) x tempo em dias).

    Perfuntar ao usuário:
    - valor normal da prestaçõa
    - taxa de juros
    - tempo em dias

    resposta:

    - valor da prestação em atraso
'''

valor = float(input("Qual o valor normal da prestação? "))
taxa = float(input("Qual a taxa de juros? "))
tempo = float(input("Quantos dias de atraso? "))

prestacao = valor + (valor * (taxa/ 100) * tempo)

print("O valor de prestação e de atraso é R$", prestacao)
