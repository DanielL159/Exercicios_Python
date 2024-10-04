"""
Exercício Python 6: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""

from math import cos, sin, tan, radians  # Importa as funções cos, sin, tan e radians do módulo math

# Solicita ao usuário que insira um ângulo em graus e converte a entrada para um inteiro.
n = int(input('Give me an angle in degrees: '))

# Calcula o seno, cosseno e tangente do ângulo.
# A função radians converte o ângulo de graus para radianos, que é o formato necessário para as funções trigonométricas.
print(f"""
Sine: {sin(radians(n))}  # Calcula o seno do ângulo.
Cosine: {cos(radians(n))}  # Calcula o cosseno do ângulo.
Tangent: {tan(radians(n)):.2f}  # Calcula e formata a tangente do ângulo com duas casas decimais.
""")
