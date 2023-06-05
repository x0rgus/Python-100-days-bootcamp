def format_name(f_name, l_name):
    full_name = (f_name + " " + l_name).title()
    return full_name

first = input("Please type the first name. ")
last = input("Please type the last name. ")

# output variable contains return values from function.
output = format_name(first, last)
print(output)