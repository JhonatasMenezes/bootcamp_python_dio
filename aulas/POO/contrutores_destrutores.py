# double underscore ou dunder = __algcoisa__

class Cachorro:
    def __init__(self, nome, cor, acordado=True) -> None:
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self. acordado = acordado

    def __del__(self):
        print("Removendo instância da classe")

    def falar(self):
        print("au auuu")


c = Cachorro("Malandrao", "amarelo")
c.falar()

print("aloooooooooooooooooou")