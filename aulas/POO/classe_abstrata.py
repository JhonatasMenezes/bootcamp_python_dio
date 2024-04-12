from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    
    def ligar(self):
        print("ligando TV...")


    def desligar(self):
        print("desligando TV...")


class ControleArCondicionado(ControleRemoto):
    
    def ligar(self):
        print("ligando ArCondicionado...")


    def desligar(self):
        print("desligando ArCondicionado...")


controle = ControleTV()
controle.ligar()
controle.desligar()

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
