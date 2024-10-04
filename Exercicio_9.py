"""
Exercício Python 9: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""
# Solicita ao usuário que insira uma frase.
text = input('Give me a text: ')

# Exibe os resultados relacionados à letra "A" na frase.
print(f"""
The letter "A" appears {text.lower().count('a')} times in the phrase.  # Conta quantas vezes a letra "A" aparece, ignorando o caso (maiúsculas e minúsculas).
Fist time it is in {text.lower().find('a') + 1} position  # Encontra a posição da primeira ocorrência de "A" e soma 1 para mostrar em uma base 1 (usuário comum).
Last time it is in {text.lower().rfind('a') + 1} position  # Encontra a posição da última ocorrência de "A" e soma 1 para mostrar em uma base 1.
""")