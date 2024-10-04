"""
Exercício Python 2: Crie um programa que leia dois números e mostre a soma entre eles.
"""

# Solicita ao usuário que insira o primeiro número.
# A função input() exibe a mensagem especificada e espera pela entrada do usuário.
# O valor digitado pelo usuário é convertido para um inteiro usando a função int() e armazenado na variável 'n1'.
n1 = int(input('Give me one number: '))
n2 = int(input('Give another one: '))

# Calcula a soma dos dois números armazenados nas variáveis 'n1' e 'n2'.
# O resultado da soma é armazenado na variável 'result'.
result = n1+n2

# Exibe o resultado da soma na tela usando a função print().
# O valor da variável 'result' é mostrado ao usuário.
print(result)
