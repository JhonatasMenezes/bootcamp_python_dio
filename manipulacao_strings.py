# MANIPULAÇÃO DE STRINGS

curso = "pYtHon"

curso.upper() # PYTHON - Transforma todas as letras em maiúsculo

curso.lower() # python - Transforma todas as letras em minúsculo

curso.title() # Python - Primeira letra em maisc e todo resto em minusc

curso = "    Python  "

curso.strip() # Python - Remove espaços da direita e esquerda

curso.lstrip() # Python-- Remove espaços da esquerda

curso.rstrip() # ----Python - Remove espaços da direita

curso.center(10, "#") # ##Python## - Faz a string ter o tamanho colocado no 1º arg preenchendo com espaços ou com um caractere mencionado no 2º arg

".".join(curso) # P.y.t.h.o.n - Une ou reune itens de uma lista ou string e inserindo um caractere entre os itens caso requisitado entre aspas


# Interpolação de variáveis

nome = "Jhonatas"
idade = 27
profissao = "Programador"
linguagem = "Python"

## Ols Style
 # string  = %s
 # inteiro = %d
 # float   = %f

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou aprendendo a linguagem %s." % (nome, idade, profissao, linguagem))

## Format
pessoa = {
    'nome':nome,
    'idade':idade,
    'profissao':profissao,
    'linguagem':linguagem
}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou aprendendo a linguagem {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho com {2} e estou aprendendo a linguagem {3}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou aprendendo a linguagem {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou aprendendo a linguagem {linguagem}.".format(**pessoa))

## F string

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou aprendendo a linguagem {linguagem}.")

# Formatar string com F string
PI = 3.14159

print(f"Valor dr PI: {PI:.2f}") # Depois do ponto insere o numero de casas decimais a ser mostrado
print(f"Valor dr PI: {PI:10.2f}") # Antes do ponto se define a quantidade de caracteres da string e após a quantidade de casas decimais para float

## Fatiamento

nome = "Jhonatas Menezes"

nome[0] # J
nome[:5] # Jhona
nome[5:] # tas Menezes
nome[5:10] # tas M 
nome[4:12:2] # aa e
nome[::-1] # sezeneM satanohJ

## String Multiplas Linhas / String Tripla

nome = "Jhonatas"

mensagem = f"""
    Olá, meu nome é {nome},
eu estou aprendendo Python.
        Esta mensagem tem diferentes recuos.
"""
