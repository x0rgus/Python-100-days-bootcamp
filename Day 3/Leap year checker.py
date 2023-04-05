def leapcheck(year):
    if year % 4 == 0:
        result = "Leap year."
    elif year % 100 == 0:
        result = "Leap year."
    elif year % 400 == 0:
        result = "Leap year."
    else:
        result = "Not leap year."
    return result


year = int(input("which year do you want to check?"))
year = leapcheck(year)

print(year)
