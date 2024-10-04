"""
Exercício Python 3: Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele.
"""

# Solicita ao usuário que insira algum valor e armazena na variável 'a'.
a = input('Give something: ')

# Exibe uma mensagem formatada que contém informações sobre o valor inserido pelo usuário.
print(f"""
Type: {type(a)}  # Mostra o tipo do valor inserido, que será sempre <class 'str'>, pois a função input retorna uma string.
It Is Alphabetic: {a.isalpha()}  # Verifica se todos os caracteres da string são letras do alfabeto.
It is Numeric:  {a.isnumeric()}  # Verifica se todos os caracteres da string são dígitos numéricos.
It is AlphaNumeric: {a.isalnum()}  # Verifica se a string contém apenas letras e números.
It is Upper Case: {a.isupper()}  # Verifica se todos os caracteres da string estão em maiúsculas.
It is Lower Case: {a.islower()}  # Verifica se todos os caracteres da string estão em minúsculas.
It is Decimal: {a.isdecimal()}  # Verifica se todos os caracteres da string são dígitos decimais (0-9).
It is Capitalize: {a.istitle()}  # Verifica se a string está capitalizada, ou seja, se a primeira letra de cada palavra está em maiúscula.
""")