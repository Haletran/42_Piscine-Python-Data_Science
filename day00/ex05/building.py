import sys


def main(argv: str):

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) != 2 or len(sys.argv[1]) == 0):
            text = sys.stdin.read()
        else:
            text = sys.argv[1]
        spaces = sum(c.isspace() for c in text)
        upper = sum(1 for c in text if c.isupper())
        lower = sum(1 for c in text if c.islower())
        numbers = sum(1 for c in text if c.isdigit())
        characters_count = len(text)
        others = characters_count - numbers - (lower + upper) - spaces

        print(f"The text contains {characters_count} characters:")
        print(f" {upper} upper letters")
        print(f" {lower} lower letters")
        print(f" {others} punctiation marks")
        print(f" {spaces} spaces")
        print(f" {numbers} digits")

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main(sys.argv)
