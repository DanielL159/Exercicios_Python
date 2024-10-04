# Python - Conceitos Básicos
## Python: Uma Visão Geral

Python é uma linguagem de programação de alto nível, conhecida por sua simplicidade e legibilidade. Criada por **Guido van Rossum** e lançada em **1991**, Python foi projetada para ser fácil de aprender e usar, com uma sintaxe clara que incentiva boas práticas de programação.

### Principais Características:

- **Sintaxe Simples e Legível**:  
  Python possui uma sintaxe que se assemelha à linguagem humana, tornando o código mais fácil de escrever e entender, o que facilita a aprendizagem para iniciantes.

- **Interpretada**:  
  Diferente de linguagens compiladas como C ou Java, Python é uma linguagem interpretada, o que significa que o código é executado linha por linha, sem a necessidade de uma compilação prévia.

- **Multiparadigma**:  
  Python suporta programação orientada a objetos, funcional e procedural, o que oferece flexibilidade aos desenvolvedores.

- **Bibliotecas Extensas**:  
  Python tem uma vasta coleção de bibliotecas e frameworks (como **NumPy**, **Pandas**, **Flask** e **Django**), que facilitam o desenvolvimento de uma ampla gama de aplicações, desde automação e análise de dados até inteligência artificial e desenvolvimento web.

- **Comunidade Ativa**:  
  Python tem uma comunidade enorme e colaborativa, que contribui para o desenvolvimento de bibliotecas, ferramentas e suporte contínuo.

### Diferenças em Relação a Outras Linguagens:

- **Curva de Aprendizado**:  
  Python é frequentemente considerada uma das linguagens mais fáceis de aprender, em comparação com linguagens como **C++** ou **Java**, que têm sintaxes mais complexas.

- **Gerenciamento de Memória Automático**:  
  Python cuida da alocação e liberação de memória automaticamente, por meio de um sistema de coleta de lixo, enquanto linguagens como **C** exigem gerenciamento manual.

- **Versatilidade**:  
  Embora outras linguagens, como Java, também sejam multiuso, Python se destaca por sua aplicação em diversas áreas, como desenvolvimento web, automação, ciência de dados e aprendizado de máquina, sem a necessidade de mudanças significativas na linguagem.

- **Velocidade de Execução**:  
  Python tende a ser mais lento que linguagens compiladas (como **C**, **C++**, **Java**) em termos de performance, já que é interpretada. No entanto, essa desvantagem pode ser compensada pelo uso de bibliotecas otimizadas e pela facilidade de desenvolvimento.

### Conclusão:

Python se diferencia por ser uma linguagem acessível e poderosa, com foco na produtividade e facilidade de uso, sendo amplamente utilizada tanto por iniciantes quanto por profissionais.

## Variáveis em Python
Em Python, toda variável é um objeto. Abaixo estão alguns exemplos de diferentes tipos de variáveis:

```python
nome = 'SANTOS'  # String
idade = 25          # Inteiro
peso = 75.8         # Float

# Exibindo os valores
print(nome, idade, peso)  # OBS: a vírgula é usada pois idade e peso não são strings
print(f'{nome} {idade} {peso}')  # OBS: 'f' é usado para formatar os campos {} com variáveis
print(nome + str(idade) + str(peso))  # OBS: transforma números em string para concatenar

# Exemplo com format()
s = 25
print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

name = input('Me de seu nome?')
idade = input('Me de seu nome?')
peso = input('Me de seu nome?')
```



## TIPOS PRIMITIVOS :
```python
int , float , bool(True,False)  ,str()
type(name)    #OBS:retorna o tipo do objeto/variavel instanciado
```



## Operadores Aritméticos (int, float):
- `+` (Adição)
- `-` (Subtração)
- `*` (Multiplicação)
- `/` (Divisão)
- `//` (Divisão inteira ou piso)
- `%` (Resto da divisão)
- `**` (Potência)
- `n**(1/2)` (Raiz quadrada, que é a potência de um número por meio)

### Ordem de Precedência:
1. Parênteses `()`
2. Potência `**`
3. Multiplicação, Divisão, Divisão Inteira, Resto da Divisão
4. Soma e Subtração

### Exemplo de Potência com `pow()`:
```python
# Outra forma de fazer potência (pode alterar a ordem de precedência)
resultado = pow(base, expoente)
```
### Exemplo de Formatação com Float:
```python
# {:.3f} indica que o número terá 3 casas decimais após o ponto
print('Divisão é {:.3f}'.format(d))  
```

## Manipulação de String 
### (Por padrão, uma string é imutável)

- `frase.count('o')`  
  **OBS**: Conta o número de vezes que a letra 'o' aparece na string. **Case sensitive**.
  
- `frase.find('deo')`  
  **OBS**: Retorna o índice de início da sequência 'deo'. Se não encontrar, retorna `-1`.

- `'Case' in frase`  
  **OBS**: Retorna `True` se a palavra 'Case' estiver presente na string `frase`.

- `frase.replace('Python', 'Androide')`  
  **OBS**: Localiza e substitui 'Python' por 'Androide' na string.

- `frase.upper()`  
  **OBS**: Converte todos os caracteres da string para maiúsculas.

- `frase.lower()`  
  **OBS**: Converte todos os caracteres da string para minúsculas.

- `frase.capitalize()`  
  **OBS**: Converte apenas a primeira letra da primeira palavra para maiúscula.

- `frase.title()`  
  **OBS**: Converte a primeira letra de cada palavra da string para maiúscula.

- `frase.strip()`  
  **OBS**: Remove espaços em branco no início e no final da string.

- `frase.rstrip()`  
  **OBS**: Remove espaços em branco à direita (final) da string.

- `frase.lstrip()`  
  **OBS**: Remove espaços em branco à esquerda (início) da string.

- `frase.split()`  
  **OBS**: Divide a string em uma lista de palavras, utilizando o espaço como delimitador por padrão para gerar essa lista
- `'-'.join(frase)`  
  **OBS**: Junta os componentes da lista em uma string, colocando um hífen `-` entre eles.

- `'Santos' in nome`  
  **OBS**: Retorna `True` se 'Santos' estiver presente na variável `nome`.


## Condição Simplificada (Operador Ternário)

Em Python, a **condição simplificada** funciona de forma semelhante ao **operador ternário** em outras linguagens. Ela permite atribuir um valor ou imprimir um resultado com base em uma condição, tudo em uma única linha de código.

### Exemplos:

- `print('carro novo' if tempo <= 3 else 'carro velho')`  
  **OBS**: Se a variável `tempo` for menor ou igual a 3, a saída será "carro novo". Caso contrário, será "carro velho".

- `print('Possível Triângulo' if a + b > c and a + c > b and b + c > a else 'Não é Triângulo')`  
  **OBS**: Verifica se a soma dos lados forma um triângulo. Se a condição for verdadeira, imprime "Possível Triângulo". Caso contrário, imprime "Não é Triângulo".

---

Para mais exemplos avançados, você pode conferir este [link sobre list comprehensions](https://pythonacademy.com.br/blog/list-comprehensions-no-python), que complementa a lógica de operadores e condições em Python.
