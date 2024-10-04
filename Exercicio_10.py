"""
Exercício Python 10: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

fullName = input('Please provide your full name: ').strip()
print(f"""
Nice to meet you {fullName.split()[0]}
Your last name is: {fullName.split()[-1]}
""")
