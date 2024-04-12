class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando vruuum')

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado) -> None:
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} estou carregado')    



moto = Motocicleta("preta", "ABC1E34", 2)
moto.ligar_motor()

carro = Carro("branco", "XDE0Q98", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "DPU0O78", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)