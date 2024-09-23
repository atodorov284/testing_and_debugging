import unittest
from unittest.mock import patch
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from src.codemaker import Codemaker  # noqa: E402


class TestCodemaker(unittest.TestCase):
    def setUp(self):
        self.codemaker = Codemaker()

    def test_symbols_property(self):
        expected_symbols = ["W", "B", "Y", "G", "R", "K"]
        self.assertEqual(self.codemaker.symbols, expected_symbols)

    def test_code_length_property(self):
        max_code_length = 4
        self.assertEqual(self.codemaker.code_length, max_code_length)

    @patch("random.choice")
    def test_generate_code(self, mock_random_choice):
        # Mock random.choice to return a deterministic code
        mock_random_choice.side_effect = ["W", "B", "G", "Y"]

        codemaker = Codemaker()

        self.assertEqual(codemaker.secret_code, ["W", "B", "G", "Y"])

        max_code_length = 4

        # Check if random.choice was called the correct number of times

        self.assertEqual(mock_random_choice.call_count, max_code_length)

    @patch("random.choice")
    def test_secret_code_is_deepcopy(self, mock_random_choice):
        # Mock random.choice to return a deterministic code
        mock_random_choice.side_effect = ["R", "G", "B", "Y"]

        codemaker = Codemaker()

        # Ensure deepcopy is returned
        secret_code_copy = codemaker.secret_code
        secret_code_copy[0] = "W"

        # Original code should not be modified
        self.assertNotEqual(codemaker.secret_code[0], "W")


if __name__ == "__main__":
    unittest.main()
