import sys
import os
from pydantic import PrivateAttr

currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, currentdir)

from codemaker import Codemaker
from codebreaker import Codebreaker


class Mastermind:
    def __init__(self, max_attempts: int) -> None:
        self.__codemaker = Codemaker()
        self.__codebreaker = Codebreaker()
        self.__max_attempts = max_attempts

    @property
    def max_attempts(self):
        return self.__max_attempts

    @property
    def codemaker(self):
        return self.__codemaker

    @property
    def codebreaker(self):
        return self.__codebreaker

    def _evaluate_guess(self, guess: list) -> tuple[int, int]:
        correct_positions = sum(
            a == b for a, b in zip(guess, self.codemaker.secret_code)
        )

        secret_code_copy = list(self.codemaker.secret_code)

        for i, symbol in enumerate(guess):
            if symbol == self.codemaker.secret_code[i]:
                secret_code_copy[i] = None

        correct_colors = 0
        for i, symbol in enumerate(guess):
            if symbol in secret_code_copy and symbol != self.codemaker.secret_code[i]:
                correct_colors += 1
                secret_code_copy.remove(symbol)

        return correct_positions, correct_colors

    def play(self) -> None:
        for attempt in range(1, self.max_attempts + 1):
            guess = self.codebreaker.make_guess()
            correct_positions, correct_color = self._evaluate_guess(guess)
            print(
                f"Attempt {attempt}: {correct_positions} correct positions, {correct_color} correct colors in the wrong position."
            )

            if correct_positions == 4:
                print(f"You won in {attempt}! You cracked the code!")
                return

        print(f"Game over. The code was {self.codemaker.secret_code}.")
