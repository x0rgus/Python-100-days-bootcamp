def prime_checker(number):
    flag = False
    if number == 1:
        print("It's not a prime number.")
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break

        if flag:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)