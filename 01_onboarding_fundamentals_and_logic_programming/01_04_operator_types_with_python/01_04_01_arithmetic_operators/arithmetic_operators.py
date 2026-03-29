# Variables
default_operator_separator = '=' * 120
default_operator_sub_separator = '-' * 120
indentation_second_level = '\t' * 1
indentation_third_level = '\t' * 2
number1 = 10
number2 = 5
result = 0

print('Arithmetic Operators in Python')


# =====================================================================================
print(default_operator_separator)
print("Addition Operator '+'")

result = number1 + number2
print(
    indentation_second_level
    + f'|==> number1({number1}) + number2({number2})\t\t\t\t\t\t\t\t= ',
    result,
)

number2 = -5
result = number1 + number2
print(
    indentation_second_level
    + f'|==> number1({number1}) + number2({number2})\t\t\t\t\t\t\t\t= ',
    result,
)

number1 = -10
result = number1 + number2
print(
    indentation_second_level
    + f'|==> With both negative numbers number1({number1}) + number2({number2}) \t\t\t\t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
print(default_operator_sub_separator)
number3 = 0.123456789
number4 = 0.2468

result = number3 + number4
# No loss of precision was observed; Consequently,  the number of  precision digits  remained the same
print(indentation_third_level + 'With just float numbers:')
print(
    indentation_third_level
    + f'|==> number3({number3}) + number4({number4})\t\t\t\t\t= ',
    result,
)

number4 = number4 * -1
result = number3 + number4
print(
    indentation_third_level
    + f'|==> number3({number3}) + number4({number4})\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number3 + number4
print(
    indentation_third_level
    + f'|==> With both negative numbers number3({number3}) + number4({number4}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
print(default_operator_sub_separator)
number1 = number1 * -1  # restoring the value to a positive sign or value
number3 = number3 * -1  # restoring the value to a positive sign or value

result = number1 + number3
print(indentation_third_level + 'With integers and float numbers:')
print(
    indentation_third_level
    + f'|==> number1({number1}) + number3({number3})\t\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number1 + number3
print(
    indentation_third_level
    + f'|==> number1({number1}) + number3({number3})\t\t\t\t\t= ',
    result,
)

number1 = number1 * -1
result = number1 + number3
print(
    indentation_third_level
    + f'|==> With both negative numbers number1({number1}) + number3({number3}) \t\t= ',
    result,
)

# =====================================================================================
print(default_operator_separator)
print("Subtraction Operator '-'")

number1 = 10
number2 = 5

result = number1 - number2
print(
    indentation_second_level
    + f'|==> number1({number1}) - number2({number2})\t\t\t\t\t= ',
    result,
)

number2 = -5
result = number1 - number2
print(
    indentation_second_level
    + f'|==> number1({number1}) - number2({number2})\t\t\t\t\t= ',
    result,
)

number1 = -10
result = number1 - number2
print(
    indentation_second_level
    + f'|==> With both negative numbers number1({number1}) - number2({number2}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
print(default_operator_sub_separator)
number3 = number3 * -1  # restoring the value to a positive sign or value
number4 = number4 * -1  # restoring the value to a positive sign or value

# No loss of precision was observed; Consequently,  the number of  precision digits  remained the same
result = number3 - number4
print(indentation_third_level + 'With just float numbers:')
print(
    indentation_third_level
    + f'|==> number3({number3}) -  number4({number4})\t\t\t\t\t= ',
    result,
)

number4 = number4 * -1
result = number3 - number4
print(
    indentation_third_level
    + f'|==> number3({number3}) - number4({number4})\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number3 - number4
print(
    indentation_third_level
    + f'|==> With both negative numbers number3({number3}) - number4({number4}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
print(default_operator_sub_separator)
number1 = number1 * -1  # restoring the value to a positive sign or value
number3 = number3 * -1  # restoring the value to a positive sign or value

result = number1 - number3
print(indentation_third_level + 'With integers and float numbers:')
print(
    indentation_third_level
    + f'|==> number1({number1}) - number3({number3})\t\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number1 - number3
print(
    indentation_third_level
    + f'|==> number1({number1}) - number3({number3})\t\t\t\t\t= ',
    result,
)

number1 = number1 * -1
result = number1 - number3
print(
    indentation_third_level
    + f'|==> With both negative numbers number1({number1}) - number3({number3}) \t\t= ',
    result,
)

# =====================================================================================
print(default_operator_separator)
print("Multiplication  Operator '*'")

number1 = 10
number2 = 5

result = number1 * number2
print(
    indentation_second_level
    + f'|==> number1({number1}) * number2({number2})\t\t\t\t\t= ',
    result,
)

number2 = -5
result = number1 * number2
print(
    indentation_second_level
    + f'|==> number1({number1}) * number2({number2})\t\t\t\t\t= ',
    result,
)

number1 = -10
result = number1 * number2
print(
    indentation_second_level
    + f'|==> With both negative numbers number1({number1}) * number2({number2}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# I observed that there was no loss of precision for the precision digits; on the contrary,
# when necessary, the number of digits was increased to retrieve the full calculated value.
print(default_operator_sub_separator)
number3 = number3 * -1  # restoring the value to a positive sign or value
number4 = number4 * -1  # restoring the value to a positive sign or value

# No loss of precision was observed; Consequently,  the number of  precision digits  remained the same
result = number3 * number4
print(indentation_third_level + 'With just float numbers:')
print(
    indentation_third_level
    + f'|==> number3({number3}) *  number4({number4})\t\t\t\t\t= ',
    result,
)

number4 = number4 * -1
result = number3 * number4
print(
    indentation_third_level
    + f'|==> number3({number3}) * number4({number4})\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number3 * number4
print(
    indentation_third_level
    + f'|==> With both negative numbers number3({number3}) * number4({number4}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Not even in operations involving integers and floating-point numbers did the implicit conversion to the
#  data type occur, which would cause a "reduction" in the number of precision digits.
print(default_operator_sub_separator)
number1 = number1 * -1  # restoring the value to a positive sign or value
number3 = number3 * -1  # restoring the value to a positive sign or value
result = number1 * number3
print(indentation_third_level + 'With integers and float numbers:')
print(
    indentation_third_level
    + f'|==> number1({number1}) * number3({number3})\t\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number1 * number3
print(
    indentation_third_level
    + f'|==> number1({number1}) * number3({number3})\t\t\t\t\t= ',
    result,
)

number1 = number1 * -1
result = number1 * number3
print(
    indentation_third_level
    + f'|==> With both negative numbers number1({number1}) * number3({number3}) \t\t= ',
    result,
)

# =====================================================================================
print(default_operator_separator)
print("Exponentiation  Operator '**'")

number1 = 2
number2 = 3

result = number1**number2
print(
    indentation_second_level
    + f'|==> number1({number1}) ** number2({number2})\t\t\t\t\t= ',
    result,
)

number2 = -3
result = number1**number2
print(
    indentation_second_level
    + f'|==> number1({number1}) ** number2({number2})\t\t\t\t\t= ',
    result,
)

number1 = -3
result = number1**number2
print(
    indentation_second_level
    + f'|==> With both negative numbers number1({number1}) ** number2({number2}) \t= ',
    result,
)

# =====================================================================================
print(default_operator_separator)
print("Division  Operator '/'")

number1 = 10
number2 = 3

result = number1 / number2
print(
    indentation_second_level
    + f'|==> number1({number1}) / number2({number2})\t\t\t\t\t= ',
    result,
)

number2 = -3
result = number1 / number2
print(
    indentation_second_level
    + f'|==> number1({number1}) / number2({number2})\t\t\t\t\t= ',
    result,
)

number1 = -10
result = number1 / number2
print(
    indentation_second_level
    + f'|==> With both negative numbers number1({number1}) /  number2({number2}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# The same same behavior observed in the multiplication operator '*'
print(default_operator_sub_separator)
number3 = number3 * -1  # restoring the value to a positive sign or value
number4 = number4 * -1  # restoring the value to a positive sign or value

result = number3 / number4
# No loss of precision was observed; Consequently,  the number of  precision digits  remained the same
print(indentation_third_level + 'With just float numbers:')
print(
    indentation_third_level
    + f'|==> number3({number3}) / number4({number4})\t\t\t\t\t= ',
    result,
)

number4 = number4 * -1
result = number3 / number4
print(
    indentation_third_level
    + f'|==> number3({number3}) / number4({number4})\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number3 / number4
print(
    indentation_third_level
    + f'|==> With both negative numbers number3({number3}) / number4({number4}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# The same same behavior observed in the multiplication operator '*'
print(default_operator_sub_separator)
number1 = number1 * -1  # restoring the value to a positive sign or value
number3 = number3 * -1  # restoring the value to a positive sign or value

result = number1 / number3
print(indentation_third_level + 'With integers and float numbers:')
print(
    indentation_third_level
    + f'|==> number1({number1}) / number3({number3})\t\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number1 / number3
print(
    indentation_third_level
    + f'|==> number1({number1}) / number3({number3})\t\t\t\t\t= ',
    result,
)

number1 = number1 * -1
result = number1 / number3
print(
    indentation_third_level
    + f'|==> With both negative numbers number1({number1}) / number3({number3}) \t\t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
print(default_operator_sub_separator)
print(
    indentation_second_level + "Division  Operator '//' as known as the floor division"
)
print(
    indentation_second_level + 'Getting just the integer part of the division result.'
)

number1 = 10
number2 = 3

result = number1 // number2
print(
    indentation_second_level
    + indentation_second_level
    + f'|==> number1({number1}) // number2({number2})\t\t\t\t\t= ',
    result,
)


number2 = -3
result = number1 // number2
print(
    indentation_second_level
    + indentation_second_level
    + f'|==> number1({number1}) // number2({number2})\t\t\t\t\t= ',
    result,
)

number1 = -10
result = number1 // number2
print(
    indentation_second_level
    + indentation_second_level
    + f'|==> With both negative numbers number1({number1}) //  number2({number2}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
print(default_operator_sub_separator)
print(
    indentation_second_level
    + "Using the division method instead of the '/' and '%' operators."
)

number1 = 10
number2 = 3

# divmod() function returns a tuple, with "two fields"/"two properties", containing the
# quotient (integer part of the division) and the reminder (the float part of the division).
# e.g divmod(10, 3) is the same as :
#   1 - quotient   = 10//3 => 3
#   2 - reminder  = 10%3 =>
quotient, reminder = divmod(number1, number2)
print(
    indentation_second_level
    + indentation_second_level
    + f'|==> divmod(number1({number1}) ,  number2({number2})) \t= ',
    (quotient, reminder),
)


# =====================================================================================
print(default_operator_separator)
print("Mod  Operator '%'")

number1 = 10
number2 = 3

result = number1 % number2
print(
    indentation_second_level
    + f'|==> number1({number1}) % number2({number2})\t\t\t\t\t= ',
    result,
)


number2 = -3
result = number1 % number2
print(
    indentation_second_level
    + f'|==> number1({number1}) % number2({number2})\t\t\t\t\t= ',
    result,
)

number1 = -10
result = number1 % number2
print(
    indentation_second_level
    + f'|==> With both negative numbers number1({number1}) %  number2({number2}) \t= ',
    result,
)

# result = number1 %% number2 # Occurs a error ('result = number1 % number2')

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# The same same behavior observed in the multiplication operator '*'
print(default_operator_sub_separator)
number3 = number3 * -1  # restoring the value to a positive sign or value
number4 = number4 * -1  # restoring the value to a positive sign or value

result = number3 % number4
# No loss of precision was observed; Consequently,  the number of  precision digits  remained the same
print(indentation_third_level + 'With just float numbers:')
print(
    indentation_third_level
    + f'|==> number3({number3}) % number4({number4})\t\t\t\t\t= ',
    result,
)

number4 = number4 * -1
result = number3 % number4
print(
    indentation_third_level
    + f'|==> number3({number3}) % number4({number4})\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number3 % number4
print(
    indentation_third_level
    + f'|==> With both negative numbers number3({number3}) % number4({number4}) \t= ',
    result,
)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# The same same behavior observed in the multiplication operator '*'
print(default_operator_sub_separator)
number1 = number1 * -1  # restoring the value to a positive sign or value
number3 = number3 * -1  # restoring the value to a positive sign or value

result = number1 % number3
print(indentation_third_level + 'With integers and float numbers:')
print(
    indentation_third_level
    + f'|==> number1({number1}) % number3({number3})\t\t\t\t\t\t= ',
    result,
)

number3 = number3 * -1
result = number1 % number3
print(
    indentation_third_level
    + f'|==> number1({number1}) % number3({number3})\t\t\t\t\t= ',
    result,
)

number1 = number1 * -1
result = number1 % number3
print(
    indentation_third_level
    + f'|==> With both negative numbers number1({number1}) % number3({number3}) \t\t= ',
    result,
)
