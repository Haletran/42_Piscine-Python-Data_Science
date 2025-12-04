import sys



def main(argv: str):
    try:
        assert len(sys.argv) == 2, "more than one or none argument is provided"
        for char in sys.argv[1]:
            assert char.isalnum() or char.isspace(), "the arguments are bad"
            
        NESTED_MORSE = {
            " ": "/ ",
            "A": ".- ", "a": ".- ",
            "B": "-... ", "b": "-... ",
            "C": "-.-. ", "c": "-.-. ",
            "D": "-.. ", "d": "-.. ",
            "E": ". ", "e": ". ",
            "F": "..-. ", "f": "..-. ",
            "G": "--. ", "g": "--. ",
            "H": ".... ", "h": ".... ",
            "I": ".. ", "i": ".. ",
            "J": ".--- ", "j": ".--- ",
            "K": "-.- ", "k": "-.- ",
            "L": ".-.. ", "l": ".-.. ",
            "M": "-- ", "m": "-- ",
            "N": "-. ", "n": "-. ",
            "O": "--- ", "o": "--- ",
            "P": ".--. ", "p": ".--. ",
            "Q": "--.- ", "q": "--.- ",
            "R": ".-. ", "r": ".-. ",
            "S": "... ", "s": "... ",
            "T": "- ", "t": "- ",
            "U": "..- ", "u": "..- ",
            "V": "...- ", "v": "...- ",
            "W": ".-- ", "w": ".-- ",
            "X": "-..- ", "x": "-..- ",
            "Y": "-.-- ", "y": "-.-- ",
            "Z": "--.. ", "z": "--.. ",
            "0": "----- ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
        }
        morse = ""
        for char in sys.argv[1]:
            morse += NESTED_MORSE.get(char.upper(), "")
        print(f"{morse}")

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main(sys.argv)
