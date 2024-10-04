"""
Exercício Python 7: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
from random import choice  # Importa a função choice do módulo random para seleção aleatória

# Solicita ao usuário que insira três nomes
studentA = input('Give me a first name: ')
studentB = input('Give me a second name: ')
studentC = input('Give me a third name: ')

# Cria uma lista chamada classroom que contém os nomes dos estudantes
classroom = [studentA, studentB, studentC]

# Usa a função choice para escolher aleatoriamente um nome da lista classroom e exibe o resultado
print(f'I chose the student {choice(classroom)}')