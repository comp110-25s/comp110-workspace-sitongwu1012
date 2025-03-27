"""Let us play wordle"""

__author__: str = "730826007"


def contains_char(search_string: str, char: str) -> bool:
    """Whether there is this letter in the word"""
    assert len(char) == 1, f"len('{char}') is not 1"

    index: int = 0
    while index < len(search_string):
        if search_string[index] == char:
            return True
        index += 1

    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns an emoji string showing the correctness of the guess."""
    assert len(guess) == len(secret), "Guess must be the same length as secret"

    result: str = ""
    index: int = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1

    return result


def input_guess(expected_length: int) -> str:
    """Prompts for a word of the expected length until valid."""
    guess: str = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The entry point of the program and main game loop."""
    turns: int = 1
    max_turns: int = 6

    while turns <= max_turns:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(len(secret))

        emoji_result = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            return

        turns += 1

    print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
