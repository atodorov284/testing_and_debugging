class Codebreaker:
    def __init__(self) -> None:
        self.__num_of_characters = 4

    def make_guess(self) -> list:
        while True:
            guess = input(
                "Enter your guess from the following letters : \
                W, B, Y, G, R, K. (e.g., WYBR): "
            ).upper()
            if (
                all(char in ["W", "B", "Y", "G", "R", "K"] for char in guess)
                and len(guess) == self.__num_of_characters
            ):
                return list(guess)
            print(
                "Invalid input. Please use only W, B, Y, G, R, K and ensure the guess is 4 symbols long."
            )
