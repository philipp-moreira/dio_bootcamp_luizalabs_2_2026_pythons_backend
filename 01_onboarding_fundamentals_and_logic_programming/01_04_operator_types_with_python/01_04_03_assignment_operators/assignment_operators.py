# Variables
result_calculation, number1, number2 = 0, 4, 6

print(f'result_calculation = {result_calculation}')
print(f'number1 = {number1}')
print(f'number2 = {number2}')

result_calculation += number1
print(f'result_calculation += number1\t==> {result_calculation}')

result_calculation -= number2
print(f'result_calculation -= number2\t==> {result_calculation}')

result_calculation **= number1
print(f'result_calculation **= number1\t==> {result_calculation}')

result_calculation *= 2
print(f'result_calculation *= 2\t\t==> {result_calculation}')

result_calculation /= 3
print(f'result_calculation /= 3\t\t==> {result_calculation}')

result_calculation = 32  # restoring the value to expression 'result_calculation *= 2' to demonstrate the behavior of the floor division operator '//'
result_calculation //= 3
print(f'result_calculation //= 3\t==> {result_calculation}')

result_calculation = 32  # restoring the value to expression 'result_calculation *= 2' to demonstrate the behavior of the mod operator '%'
result_calculation %= 3
print(f'result_calculation %= 3\t\t==> {result_calculation}')
