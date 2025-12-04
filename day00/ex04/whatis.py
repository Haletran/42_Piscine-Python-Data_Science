import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if (len(sys.argv) == 2):
        assert int(sys.argv[1]), "argument is not an integer"
        number = int(sys.argv[1])
        if (number % 2 == 0):
            print("Is Even")
        else:
            print("Is Odd")
except (AssertionError, ValueError) as error:
    print(f"AssertionError: {error}")

