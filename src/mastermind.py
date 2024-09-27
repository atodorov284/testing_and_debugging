import sys
import os
from pydantic import PrivateAttr

currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, currentdir)

from codemaker import Codemaker  # noqa: E402
from codebreaker import Codebreaker  # noqa: E402


class Mastermind:
    __codemaker: Codemaker = PrivateAttr()
    __codebreaker: Codebreaker = PrivateAttr()
    __max_attempts: int = PrivateAttr()

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

        correct_colors = sum(
            a in self.codemaker.secret_code and a != b
            for a, b in zip(guess, self.codemaker.secret_code)
        )

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
