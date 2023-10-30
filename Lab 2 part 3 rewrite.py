number = []
while len(number) < 3:
    num = input("Please enter a 4 digit number ")
    if num.isdigit():
        if num in range(1000, 10000):
            number.append(num)
        else:
            print("Please input a 4 digit number ")
    else:
        print("Please input a number ")

print(str(number.max()) + " is the largest out of all")