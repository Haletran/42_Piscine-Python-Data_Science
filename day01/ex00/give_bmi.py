# BMI (body mass index in french IMC)

def give_bmi(height: list[int | float], weight: list[int | float]):
    result = []

    try:
        if len(height) != len(weight):
            raise ValueError("both list are not the same size")
        for i in range(len(height)):
            if not isinstance(height[i], (int, float)):
                raise ValueError("height not an int or float")
            if not isinstance(weight[i], (int, float)):
                raise ValueError("weight not an int or float")
            result.append(weight[i] / (height[i] ** 2))
        return result
    except ValueError as error:
        print(f"Error: {error}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    result = []

    try:
        for i in range(len(bmi)):
            if (bmi[i] > limit):
                result.append(True)
            elif (bmi[i] < limit):
                result.append(False)
        return result
    except ValueError as error:
        print(f"Error: {error}")
