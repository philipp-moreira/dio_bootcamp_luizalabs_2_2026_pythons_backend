# Variables
default_operator_separator = '=' * 120
default_operator_sub_separator = '-' * 120
indentation_first_level = ''
indentation_second_level = '\t' * 1
balance = 400.00
withdraw_money = 120.00
check = False

print(f'balance = {balance}')
print(f'withdraw_money = {withdraw_money}')

print(default_operator_separator)
print("'and' operator")

check = withdraw_money > 0 and balance >= withdraw_money
print(
    f"Expression with 'and' operator ' withdraw_money > 0 and balance >= withdraw_money' is equal to:\t\t{check}"
)
check = True and True
print(f"Expression with 'and' operator 'True and True' is equal to:\t\t\t\t{check}")
check = False and True
print(f"Expression with 'and' operator 'False and True' is equal to:\t\t\t\t{check}")
check = False & True
print(
    indentation_second_level
    + f"Expression with '& [bitwise]' operator 'False & True' is equal to:\t\t{check}"
)
check = True and False
print(f"Expression with 'and' operator 'True and False' is equal to:\t\t\t\t{check}")
check = False and False
print(f"Expression with 'and' operator 'False and False' is equal to:\t\t\t\t{check}")

print(default_operator_separator)
print("'or' operator")
check = withdraw_money > 0 and balance >= withdraw_money
print(
    f"Expression with 'and' operator ' withdraw_money > 0 and balance >= withdraw_money' is equal to:\t\t{check}"
)
balance = -10.00
withdraw_money = -1.00
print(f'balance = {balance}')
print(f'withdraw_money = {withdraw_money}')

check = withdraw_money > 0 or balance >= withdraw_money
print(
    f"Expression with 'and' operator ' withdraw_money > 0 and balance >= withdraw_money' is equal to:\t\t{check}"
)
check = True or True
print(f"Expression with 'or' operator 'True or True' is equal to:\t\t\t\t{check}")

check = False or True
print(f"Expression with 'or' operator 'False or True' is equal to:\t\t\t\t{check}")
check = False | True
print(
    indentation_second_level
    + f"Expression with '| [bitwise]' operator 'False | True' is equal to:\t\t\t\t{check}"
)
check = True or False
print(f"Expression with 'or' operator 'True or False' is equal to:\t\t\t\t{check}")
check = False or False
print(f"Expression with 'or' operator 'False or False' is equal to:\t\t\t\t{check}")

balance = 400.00
withdraw_money = 120.00
print(f'balance = {balance}')
print(f'withdraw_money = {withdraw_money}')

print(default_operator_separator)
print("'not' operator")

my_empty_list = []
my_empty_string = ''
my_empty_string_with_spaces = ' '
print(f'my_empty_list = [] ==> {my_empty_list}')
print(f'my_empty_string = "" ==> {my_empty_string}')
print(f'my_empty_string_with_spaces = " " ==> {my_empty_string_with_spaces}')

check = not withdraw_money > balance
print(
    f"Expression with 'not' operator 'not withdraw_money > balance ' is equal to:\t\t{check}"
)
check = not True
print(f"Expression with 'not' operator 'not True' is equal to:\t\t\t\t{check}")
check = not False
print(f"Expression with 'not' operator 'not False' is equal to:\t\t\t\t{check}")
check = True ^ False
print(
    indentation_second_level
    + f"Expression with '^ [bitwise]' operator ' True ^ False' is equal to:\t\t{check}"
)

check = not my_empty_list
print(f"Expression with 'not' operator ' not my_empty_list' is equal to:\t\t{check}")

if not my_empty_list:
    my_empty_list.append('new item1')

print('if not my_empty_list:')
print("    my_empty_list.append('new item1')")
print(f'my_empty_list = [] ==> {my_empty_list}')


check = not my_empty_list
print(f"Expression with 'not' operator ' not my_empty_list' is equal to:\t\t{check}")

check = not my_empty_string
print(f"Expression with 'not' operator ' not  my_empty_string' is equal to:\t\t{check}")
check = not my_empty_string_with_spaces
print(
    f"Expression with 'not' operator ' not  my_empty_string_with_spaces' is equal to:\t{check}"
)

print('Other uses to logic operators')
print(f"None and 'default = > {None and 'default'}")
print(indentation_second_level + f"'value' and 'default' = > {'value' and 'default'}")
print(f"None or 'default = > {None or 'default'}")
print(indentation_second_level + f"'value' or 'default' = > {'value' or 'default'}")
