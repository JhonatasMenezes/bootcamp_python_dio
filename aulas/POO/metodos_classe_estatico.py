class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_por_data_nascimento(cls, ano, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_por_data_nascimento(1997, "Jhonatas")
print(p.nome, p.idade)
print(p.maior_idade(p.idade))

