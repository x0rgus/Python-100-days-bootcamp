height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / (float(height) ** 2)
bmi = round(bmi)
str(bmi)
print(bmi)
group = ""
if bmi <= 18.5:
    group = "underweight"
elif bmi <= 25:
    group = "normal weight"
elif bmi <= 30:
    group = "slightly overweight"
elif bmi <= 35:
    group = "obese"
else:
    group = "clinically obese"


print(f"Your BMI is {bmi}, you are {group}")