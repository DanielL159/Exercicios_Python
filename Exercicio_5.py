"""
Exercício Python 5: Crie um programa que leia um número Real
qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
import math  # Importa o módulo math que contém funções matemáticas

# Solicita ao usuário que insira um número real e converte a entrada para um float.
n = float(input('Give a number: '))

# Usa a função math.trunc() para obter a parte inteira do número real e a exibe na tela.
# A função trunc() remove a parte decimal do número, retornando apenas a parte inteira.
print(f'The integer part is: {math.trunc(n)}')