"""
Exercício Python 8: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""
# Solicita ao usuário que forneça seu nome completo.
# A função 'input()' captura a entrada do usuário como uma string e a armazena na variável 'name'.
name = input('Please provide your full name: ')

# Exibe informações sobre o nome fornecido em um formato multi-linha.
print(f"""
Uppercase name: {name.upper()}  # Converte todas as letras do nome para maiúsculas usando o método 'upper()'.
Lowercase name: {name.lower()}  # Converte todas as letras do nome para minúsculas usando o método 'lower()'.
Total number of letters: {len(name) - name.count(' ')}  # Conta o total de caracteres na string 'name' subtraindo o número de espaços.
Number of letters in the first name: {len(name.split()[0])}  # Conta o número de letras no primeiro nome.
""")