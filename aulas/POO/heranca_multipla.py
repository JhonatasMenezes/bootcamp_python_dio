class Animal:
    def __init__(self, numero_patas) -> None:
        self.numero_patas = numero_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo



class Ave(Animal):
    def __init__(self, cor_bico,  **kwargs) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas) -> None:
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, numero_patas=numero_patas)
        


gato = Gato(numero_patas=4, cor_pelo="preto")
print(gato)

ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)

