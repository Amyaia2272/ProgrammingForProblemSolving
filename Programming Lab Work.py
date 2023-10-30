# Part 1
my_age = 18
friend_age = 17
total_age = my_age + friend_age
favorite_color = 'Royal Blue'
print("My favorite color is " + favorite_color + "\n")

# Part 2
username = str.title(input())
print("Hello there, " + username + " and welcome to my program\n")

# Part 3
word = input()
print(word.upper())
print(word[:5])
print(word[1] + word[4])

# Part 4
num = float(input())
print("\n" + str(num) + " doubled becomes " + str(num * num))

# Part 5
car = ["Porsche", "Chevy", "Honda", "Hundai", "Toyota"]
for i in car:
    print(i + " makes cars\n")

"""
for num in range(1, 6) would run the for loop 6 times and will print the numbers 1, 2, 3, 4, 5, and 6
"""

# Part 6
user_age = int(input("\nPlease enter your age\n"))
if user_age >= 18:
    print("You are able to vote")
else:
    print("You are currently unable to vote")