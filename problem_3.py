n1 = int(input()) # Don't change this line
n2 = int(input()) # Don't change this line
op = input() # Don't change this line
result = 0
if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '/':
    result = n1 / n2
elif op == '*':
    result = n1 * n2
else:
    result = "Invalid operator"

print("The result is:", result)