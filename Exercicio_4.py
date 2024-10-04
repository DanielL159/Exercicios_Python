"""
Exercício Python 4: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

# Solicita ao usuário a quantidade de dias que o carro foi alugado e converte a entrada para um inteiro.
day = int(input('How many days was this car rented for? '))

# Solicita ao usuário a quantidade de quilômetros percorridos pelo carro e converte a entrada para um float.
km = float(input('How many kilometers were traveled? '))

# Calcula o valor total a pagar, multiplicando o número de dias pelo custo diário e somando ao custo dos quilômetros rodados.
# O carro custa R$60 por dia e R$0,15 por Km rodado.
total_amount = (day * 60) + (km * 0.15)

# Exibe o valor total a ser pago pelo aluguel do carro.
print('Amount to pay: {}'.format(total_amount))