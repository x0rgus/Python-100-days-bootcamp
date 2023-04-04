print("basic calculators")
print("Choose by typing the corresponding number")
print("1-Two digit calculator")
print("2-BMI calculator")
print("")
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
    heighttemp = float(height)
    weighttemp = int(weight)
    bmi = weighttemp / (heighttemp * heighttemp)
    bmi = round(bmi)
    str(bmi)
    print(bmi)