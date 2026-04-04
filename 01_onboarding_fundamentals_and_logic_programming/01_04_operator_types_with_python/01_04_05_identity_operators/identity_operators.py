number_integer_1 = 8
number_integer_2 = 8
print('number_integer_1 = 8')
print('number_integer_2 = 8')


print(f'number_integer_1 == 8  => {number_integer_1 == 8}')
print(f'number_integer_2 == 8  => {number_integer_2 == 8}')
print(f'number_integer_1 == number_integer_2 => {number_integer_1 == number_integer_2}')

print(
    f'number_integer_1 is 8  => {number_integer_1 is 8}'
)  # Ruff's warning "Use `==` to compare constant literals"
print(
    f'number_integer_2 is 8  => {number_integer_2 is 8}'
)  # Ruff's warning "Use `==` to compare constant literals"
print(f'number_integer_1 is number_integer_2 => {number_integer_1 is number_integer_2}')


large_number_integer_3 = 12344567890
large_number_integer_4 = 12344567890
print('large_number_integer_3 = 12344567890')
print('large_number_integer_4 = 12344567890')


print(f'large_number_integer_3 == 8  => {large_number_integer_3 == 8}')
print(f'large_number_integer_4 == 8  => {large_number_integer_4 == 8}')
print(
    f'large_number_integer_3 == large_number_integer_4 => {large_number_integer_3 == large_number_integer_4}'
)

print(
    f'large_number_integer_3 is 8  => {large_number_integer_3 is 12344567890}'
)  # Ruff's warning "Use `==` to compare constant literals"
print(
    f'large_number_integer_4 is 8  => {large_number_integer_4 is 12344567890}'
)  # Ruff's warning "Use `==` to compare constant literals"
print(
    f'large_number_integer_3 is large_number_integer_4 => {large_number_integer_3 is large_number_integer_4}'
)

text_str_lower_lower_case = 'lorem ipsum'
text_str_lower_upper_case = 'LOREM IPSUM'

print("text_str_lower_lower_case = 'lorem ipsum'")
print("text_str_lower_upper_case = 'LOREM IPSUM'")
print("text_str_lower_capitalize = 'Lorem Ipsum'")

print(
    f'text_str_lower_lower_case == text_str_lower_upper_case => {text_str_lower_lower_case == text_str_lower_upper_case}'
)
print(
    f'text_str_lower_lower_case is text_str_lower_upper_case => {text_str_lower_lower_case is text_str_lower_upper_case}'
)

print(
    f"text_str_lower_lower_case is 'lorem ipsum'  => {text_str_lower_lower_case is 'lorem ipsum'}"  # Ruff's warning "Use `==` to compare constant literals"
)

large_text_str_lower_lower_case = ' lorem ipsum ' * 10000
large_text_str_lower_upper_case = 'LOREM IPSUM' * 10000

print("large_text_str_lower_lower_case = ' lorem ipsum ' * 10000")
print("large_text_str_lower_upper_case = 'LOREM IPSUM' * 10000")

print(
    f'large_text_str_lower_lower_case == large_text_str_lower_upper_case => {large_text_str_lower_lower_case == large_text_str_lower_upper_case}'
)
print(
    f'large_text_str_lower_lower_case is large_text_str_lower_upper_case => {large_text_str_lower_lower_case is large_text_str_lower_upper_case}'
)

print(
    f"large_text_str_lower_lower_case is ' lorem ipsum ' * 10000  => {large_text_str_lower_lower_case is ' lorem ipsum ' * 10000}"
)
