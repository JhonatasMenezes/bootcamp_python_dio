# Funções no python

def exemplo_de_funcao_sem_params():
    print("Eu não tenho parâmetros :((((")

def exibir_mensagem_bem_vindo(nome):
    print(f"Seja bem vindo(a) {nome}!")

def exibir_mensagem_bem_vindo(nome="Antônio"):
    print(f"Seja bem vindo(a) {nome}!")

def receber_varios_args_pra_iterar(*args, **kwargs):
    exibir_args = [arg for arg in args]
    exibir_kwargs = [kwarg for kwarg in kwargs]

    print(exibir_args, exibir_kwargs)

# Usar funções dentro de outras funções
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_mensagem(a, b, func):
    resultado = func(a, b)
    print(f"O resultado da operação é {resultado}.")

resultado1 = exibir_mensagem(1, 2, somar)
resultado2 = exibir_mensagem(2, 3, subtrair)

