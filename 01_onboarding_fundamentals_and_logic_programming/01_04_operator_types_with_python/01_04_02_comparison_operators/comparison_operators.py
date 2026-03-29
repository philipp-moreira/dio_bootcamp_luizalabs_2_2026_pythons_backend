# Variables
default_operator_separator = '=' * 120
default_operator_sub_separator = '-' * 120
indentation_first_level = ''
indentation_second_level = '\t' * 1
balance = 400.00
withdraw_money = 120.00
default_encoding_to_bytes = 'utf-8'
lower_case_string = 'learning python'
lower_case_string_with_space_in_the_end = 'learning python '
lower_case_string_bytes = bytes(lower_case_string, default_encoding_to_bytes)
upper_case_string = 'LEARNING PYTHON'
upper_case_string_bytes = bytes(upper_case_string, default_encoding_to_bytes)
result = False

print('Variables and values')
print(f'balance = {balance} ')
print(f'withdraw_money = {withdraw_money} ')

print(default_operator_separator)
print("Using the equality operator '=='")
result = balance == withdraw_money
print(
    f"The result of expression 'balance({balance}) == withdraw_money ({withdraw_money})' is: {result}"
)

# There is a difference when comparing uppercase and lowercase letters.
result = lower_case_string == upper_case_string
print(
    indentation_second_level
    + f"|--> The result of expression 'lower_case_string({lower_case_string}) == upper_case_string({upper_case_string})' is: {result}"
)

# There is also a difference when comparing lowercase letters, with only a space at the end.
result = lower_case_string == lower_case_string_with_space_in_the_end
print(
    indentation_second_level
    + f"|--> The result of expression 'lower_case_string({lower_case_string}) == lower_case_string_with_space_in_the_end({lower_case_string_with_space_in_the_end})' is: {result}"
)

result = lower_case_string_bytes == upper_case_string_bytes
print(
    indentation_second_level
    + f"|--> The result of expression 'lower_case_string_bytes({lower_case_string_bytes}) == upper_case_string_bytes({upper_case_string_bytes})' is: {result}"
)

# Essentially, there is no encoding that forces the same code/numerical representation for the same letter in lowercase and uppercase.
# In other words, this comparison behavior is not inherent to language, but rather to the context of computing itself.
print(
    indentation_second_level
    + indentation_second_level
    + f'|--> Because the value in bytes to "{lower_case_string_bytes}" is :\t{list(lower_case_string_bytes)}'
)
print(
    indentation_second_level
    + indentation_second_level
    + f'|--> Because the value in bytes to "{upper_case_string_bytes}" is :\t{list(upper_case_string_bytes)}'
)


print(default_operator_separator)
print("Using the not equal  operator '!='")
result = balance != withdraw_money
print(
    f"The result of expression 'balance({balance}) != withdraw_money ({withdraw_money})' is: {result}"
)

# There is a difference when comparing uppercase and lowercase letters.
result = lower_case_string != upper_case_string
print(
    indentation_second_level
    + f"|--> The result of expression 'lower_case_string({lower_case_string}) != upper_case_string({upper_case_string})' is: {result}"
)

# There is also a difference when comparing lowercase letters, with only a space at the end.
result = lower_case_string != lower_case_string_with_space_in_the_end
print(
    indentation_second_level
    + f"|--> The result of expression 'lower_case_string({lower_case_string}) != lower_case_string_with_space_in_the_end({lower_case_string_with_space_in_the_end})' is: {result}"
)

result = lower_case_string_bytes != upper_case_string_bytes
print(
    indentation_second_level
    + f"|--> The result of expression 'lower_case_string_bytes({lower_case_string_bytes}) != upper_case_string_bytes({upper_case_string_bytes})' is: {result}"
)

# Essentially, there is no encoding that forces the same code/numerical representation for the same letter in lowercase and uppercase.
# In other words, this comparison behavior is not inherent to language, but rather to the context of computing itself.
print(
    indentation_second_level
    + indentation_second_level
    + f'|--> Because the value in bytes to "{lower_case_string_bytes}" is :\t{list(lower_case_string_bytes)}'
)
print(
    indentation_second_level
    + indentation_second_level
    + f'|--> Because the value in bytes to "{upper_case_string_bytes}" is :\t{list(upper_case_string_bytes)}'
)


print(default_operator_separator)
print("Using the less than  operator '<'")
result = balance < withdraw_money
print(
    f"The result of expression ' balance({balance})  < withdraw_money({withdraw_money}) )' is: {result}"
)

print(default_operator_separator)
print("Using the less than or equal to  operator '<='")
result = balance <= withdraw_money
print(
    f"The result of expression ' balance({balance})  <= withdraw_money({withdraw_money}) )' is: {result}"
)
result = lower_case_string <= upper_case_string
print(
    indentation_second_level
    + f"|--> The result of expression ' lower_case_string({lower_case_string}) <= upper_case_string({upper_case_string})' is: {result}"
)

print(default_operator_separator)
print("Using the greater than  operator '>'")
result = balance > withdraw_money
print(
    f"The result of expression ' balance({balance})  > withdraw_money({withdraw_money}) )' is: {result}"
)

print(default_operator_separator)
print("Using the greater than or equal to  operator '>='")
result = balance >= withdraw_money
print(
    f"The result of expression ' balance({balance})  >= withdraw_money({withdraw_money}) )' is: {result}"
)
