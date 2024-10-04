"""
Exercício Python 1: Faça um programa que leia o nome de uma pessoa
e mostre uma mensagem de boas-vindas.
"""

# Solicita ao usuário que insira seu nome.
# A função input() exibe a mensagem especificada e espera pela entrada do usuário.
# O valor digitado pelo usuário é armazenado na variável 'name'.
name = input("What's your name? ")

# Exibe uma mensagem de boas-vindas utilizando a função print().
# O método format() é utilizado para inserir o valor da variável 'name' na string de saída.
# Assim, a mensagem será personalizada com o nome do usuário.
print('Welcome {}'.format(name))
