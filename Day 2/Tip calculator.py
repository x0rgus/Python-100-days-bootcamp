print("welcome to the tip calculator")
value = int(input(print("total value of the bill:")))
tip = input(print("what percentage tip would you like to give?(10, 12 or 15):"))
people = int(input(print("how many people splitting the bill?:")))
finalvalue = 0

if tip == "10":
    finalvalue = (value/people)*1.10
elif tip == "12":
    finalvalue = (value/people)*1.12
elif tip == "15":
    finalvalue = (value/people)*1.15
else:
    print("invalid input")
finalvalue = round(finalvalue, 2)
print(f"each person should pay:{finalvalue}")
