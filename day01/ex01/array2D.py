import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list):
            raise ValueError("not a list")
        print(f"My shape is : {np.array(family).shape}")
        new_family = family[start:end]
        print(f"My new shape is : {np.array(new_family).shape}")
        return (new_family)
    except ValueError as error:
        print(f"Error: {error}")
