def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
num1 = int(input("Please type the first number:"))
num2 = int(input("please type the second number:"))
for item in operation:
    print(item)
choice = input("Choose an operation:")

calc_func = operation[choice]
answer = calc_func(num1, num2)
print(answer)