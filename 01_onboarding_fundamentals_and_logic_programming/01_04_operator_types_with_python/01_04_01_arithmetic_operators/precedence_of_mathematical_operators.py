# Variables
number_a, number_b, number_c = 10, 5, 2  # Multiple assignment using unpacking
result, second_result, third_result = 0, 0, 0

print('Precedence Of Mathematical Operators  in Python')

result = number_a - number_b * number_c
print(
    f"The expression  ' number_a ({number_a}) - number_b ({number_b}) * number_c ({number_c})' will result in ==> {result}"
)

second_result = number_b * number_c
print(
    f"\tBecause  \t'number_b ({number_b}) \t* number_c ({number_c})' is equal to  ==> {second_result}"
)

third_result = number_a - second_result
print(
    f"\tAnd go on  \t'number_a ({number_a})  -  second_result ({second_result})' is equal to  ==> {third_result}"
)

print('Imposing order of  precedence  - With use the parenthesis')
result = (number_a - number_b) * number_c
print(
    f"The expression  ' (number_a({number_a}) - number_b({number_b})) * number_c({number_c})' will result in ==> {result}"
)

print('Without imposing an order of precedence through the use of parentheses.')
print('Mathematical precedence is followed.')

result = number_a + number_c - number_b * number_a**number_c / number_a
print(
    'First exponentiation, then multiplication and division (and if these are not enclosed in parentheses, the order of priority will be followed from left to right) and finally addition and subtraction (and again if these are not enclosed in parentheses, the order of priority will be followed from left to right).'
)
print(
    f"The expression  'number_a + number_c - number_b * number_a**number_c / number_a' will result in ==> {result}"
)
