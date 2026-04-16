class Calculator:
    def do_calculation(self, number_1, number_2, operation) -> float:
        if operation is None:
            return 0
        else:
            return operation(number_1, number_2)


def sum(number_1, number_2) -> int:
    """makes the sum of two numbers"""
    return number_1 + number_2


def subtraction(number_1, number_2) -> int:
    """subtracts two numbers"""
    return number_1 - number_2


def multiplication(number_1, number_2) -> int:
    """multiplies two numbers"""
    return number_1 * number_2


def division(number_1, number_2) -> float:
    """divides two numbers. If the second number is 0 (zero) the operation will not be performed and a value 0 (zero) will be returned."""

    if number_2 == 0:
        return number_2

    return number_1 / number_2


calculator = Calculator()

print('calculator.do_calculation(2, 2, sum)', calculator.do_calculation(2, 2, sum))
print(
    'calculator.do_calculation(2, 2, subtraction)',
    calculator.do_calculation(2, 2, subtraction),
)
print(
    'calculator.do_calculation(2, 2, multiplication)',
    calculator.do_calculation(2, 2, multiplication),
)
print(
    'calculator.do_calculation(2, 2, division)',
    calculator.do_calculation(2, 2, division),
)
print(
    'calculator.do_calculation(2, 0, division)',
    calculator.do_calculation(2, 0, division),
)
print(
    'calculator.do_calculation(2, 2, None)',
    calculator.do_calculation(2, 2, None),
)
