import unittest
from unittest.mock import MagicMock
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from src.mastermind import Mastermind  # noqa: E402


class TestMastermind(unittest.TestCase):
    def setUp(self):
        self.mock_codemaker = MagicMock()
        self.mock_codebreaker = MagicMock()

        Mastermind.codemaker = self.mock_codemaker
        Mastermind.codebreaker = self.mock_codebreaker

        self.mock_codemaker.secret_code = [1, 2, 3, 4]
        self.max_attempts = 10

        self.mastermind = Mastermind(self.max_attempts)

    def test_max_attempts_property(self):
        # See if the max_attempts property is set correctly
        self.assertEqual(self.mastermind.max_attempts, self.max_attempts)

    def test_codemaker_property(self):
        # See if the codemaker property is set correctly
        self.assertEqual(self.mastermind.codemaker, self.mock_codemaker)

    def test_codebreaker_property(self):
        # See if the codebreaker property is set correctly
        self.assertEqual(self.mastermind.codebreaker, self.mock_codebreaker)

    def test_evaluate_guess_all_correct(self):
        guess = [1, 2, 3, 4]
        self.mock_codemaker.secret_code = guess

        correct_position, correct_color = self.mastermind._evaluate_guess(guess)
        self.assertEqual(correct_position, 4)
        self.assertEqual(correct_color, 0)

    def test_evaluate_guess_partial_correct(self):
        guess = [1, 4, 2, 5]
        self.mock_codemaker.secret_code = [1, 2, 3, 4]

        correct_position, correct_color = self.mastermind._evaluate_guess(guess)
        self.assertEqual(correct_position, 1)  # Only 1 is in the correct position
        self.assertEqual(correct_color, 2)  # 4 and 2 are correct but in wrong positions

    def test_play_win(self):
        # Mock the codebreaker to always return the correct guess
        self.mock_codebreaker.make_guess.return_value = [1, 2, 3, 4]
        self.mock_codemaker.secret_code = [1, 2, 3, 4]

        # Test the play method for winning in the first attempt
        with unittest.mock.patch("builtins.print") as mocked_print:
            self.mastermind.play()

        # Check if the win message was printed
        mocked_print.assert_any_call("You won in 1! You cracked the code!")

    def test_play_lose(self):
        # Mock the codebreaker to return wrong guesses
        self.mock_codebreaker.make_guess.return_value = [0, 0, 0, 0]
        self.mock_codemaker.secret_code = [1, 2, 3, 4]

        # Test the play method for losing the game after max attempts
        with unittest.mock.patch("builtins.print") as mocked_print:
            self.mastermind.play()

        # Check if the game-over message was printed
        mocked_print.assert_any_call(
            f"Game over. The code was {self.mock_codemaker.secret_code}."
        )


if __name__ == "__main__":
    unittest.main()
