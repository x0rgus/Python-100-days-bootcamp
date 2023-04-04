print("basic calculators")
print("Choose by typing the corresponding number")
print("1-Two digit calculator")
print("2-BMI calculator")
print("3-Life in years/months/weeks")
choice = input()


if choice == "1":
    # two digit calculator
    userinput = input("Type a two digit number: ")
    if len(userinput ) <2 or len(userinput ) >2:
        print("invalid number")
    else:
        A = userinput[0]
        B = userinput[1]
        result = int(A) + int(B)
        strresult = str(result)
        print(strresult)

elif choice == "2":
    # bmi calculator
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    bmi = int(weight) / (float(height)**2)
    bmi = round(bmi)
    str(bmi)
    print(bmi)

elif choice == "3":
    age = input("What is your current age? ")
    time_remaining = 90 - int(age)
    days = time_remaining * 365
    weeks = time_remaining * 52
    months = time_remaining * 12
    print(f"You have {days} days, {weeks} weeks, and {months} months left.")