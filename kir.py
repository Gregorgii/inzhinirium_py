import re

expression = '123+321+2+5/2'

elements = re.findall(r'(\d+|\+|\-|\*|\/)', expression)

numbers = []
operators = []
for element in elements:
    if element.isdigit():
        numbers.append(int(element))
    else:
        operators.append(element)

result = numbers[0]
for i in range(1, len(numbers)):
    if operators[i-1] == '+':
        result += numbers[i]
    elif operators[i-1] == '-':
        result -= numbers[i]
    elif operators[i-1] == '*':
        result *= numbers[i]
    elif operators[i-1] == '/':
        result /= numbers[i]

print(result) 
