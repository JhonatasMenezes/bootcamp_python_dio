from typing import Dict
from .customer import Customer


class PhysicalPerson(Customer):
    def __init__(self, cpf: str, name: str, birth_date: str, address: Dict) -> None:
        super().__init__(address)
        self.__name = name
        self.__cpf = cpf
        self.__birth_date = birth_date
        

    @property
    def name(self):
        return self.__name


    @property
    def cpf(self):
        return self.__cpf


    @property
    def birth_date(self):
        return self.__birth_date
