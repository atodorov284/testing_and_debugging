import unittest
from unittest.mock import patch
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from src.codebreaker import Codebreaker  # noqa: E402


class TestCodebreaker(unittest.TestCase):
    @patch("builtins.input", side_effect=["WYBR"])
    def test_make_guess_valid_input(self, mock_input):
        # Test that the valid input 'WYBR' returns the expected guess

        codebreaker = Codebreaker()
        guess = codebreaker.make_guess()
        self.assertEqual(guess, ["W", "Y", "B", "R"])

    @patch("builtins.input", side_effect=["kgRW"])
    def test_make_guess_valid_lowercase(self, mock_input):
        # Lowercase converted to uppercase
        codebreaker = Codebreaker()
        guess = codebreaker.make_guess()
        self.assertEqual(guess, ["K", "G", "R", "W"])

    @patch("builtins.input", side_effect=["WRONG", "BBB", "WRYR"])
    def test_make_guess_invalid_multiple_times(self, mock_input):
        # Test multiple invalid inputs and finally a valid one
        codebreaker = Codebreaker()

        with patch("builtins.print") as mock_print:
            guess = codebreaker.make_guess()

        # Two times invalid
        mock_print.assert_called_with(
            "Invalid input. Please use only W, B, Y, G, R, K and ensure the guess is 4 symbols long."
        )

        # Last one valid
        self.assertEqual(guess, ["W", "R", "Y", "R"])


if __name__ == "__main__":
    unittest.main()
