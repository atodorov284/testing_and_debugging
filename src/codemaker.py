import random
from pydantic import PrivateAttr
from copy import deepcopy


class Codemaker:
    __symbols: list = PrivateAttr()
    __code_length: int = PrivateAttr()
    __secret_code: list = PrivateAttr()

    def __init__(self) -> None:
        self.__symbols = ["W", "B", "Y", "G", "R", "K"]
        self.__code_length = 4
        self.__secret_code = self.__generate_code()

    @property
    def symbols(self):
        return self.__symbols

    @property
    def code_length(self):
        return self.__code_length

    @property
    def secret_code(self):
        return deepcopy(self.__secret_code)

    def __generate_code(self) -> list:
        return [random.choice(self.symbols) for _ in range(self.code_length)]
