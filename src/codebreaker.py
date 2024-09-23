class Codebreaker:
    def __init__(self) -> None:
        pass

    def make_guess(self) -> list:
        while True:
            guess = input(
                "Enter your guess from the following letters : \
                W, B, Y, G, R, K. (e.g., WYBR): "
            ).upper()
            if (
                all(char in ["W", "B", "Y", "G", "R", "K"] for char in guess)
                and len(guess) == 4
            ):
                return list(guess)
            print(
                "Invalid input. Please use only W, B, Y, G, R, K and ensure the guess is 4 symbols long."
            )
