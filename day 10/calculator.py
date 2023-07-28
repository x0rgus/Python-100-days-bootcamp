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
def calculation():
    runflag = True
    while runflag == True:
        num1 = int(input("Please type the first number:"))
        num2 = int(input("please type the second number:"))
        for item in operation:
            print(item)
        choice = input("Choose an operation:")

        calc_func = operation[choice]
        answer = calc_func(num1, num2)
        print(f"{num1}{choice}{num2}={answer}")

        choice = input("Pick another operation:")
        calc_func = operation[choice]
        num3 = int(input("pick another number:"))
        answer = calc_func(answer, num3)
        print(answer)
        cont = input("do another calculation? y/n (type new for a new calculation)").lower()
        if cont == "y":
            runflag = True
            continue
        elif cont == "n":
            runflag = False
            break
        elif cont == "new":
            calculation()
calculation()