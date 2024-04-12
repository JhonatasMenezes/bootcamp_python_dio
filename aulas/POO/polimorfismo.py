class Passaro:
    def voar(self):
        print("Voaando...")


class Pardal(Passaro):
    def voar(self):
        super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


# FIXME: exemplo ruim do uso de heraça para adotar o método voar()
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando ...")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
