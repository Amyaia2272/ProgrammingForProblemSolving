#Midterm Code
#Part 1
age = int(input("Please enter your age\n"))
name = str.title(input("Please enter your name\n"))
if age < 18:
    print("I'm sorry " + name + " but please come back when you are 18.")
else:
    print("Welcome " + name + " to the system.")

#Part 2
def user_welcome(age, name):
    if age < 18:
        print("I'm sorry " + name + " but please come back when you are 18.")
    else:
        print("Welcome " + name + " to the system.")

a = int(input("Please enter your age\n"))
n = str.title(input("Please enter your name\n"))
user_welcome(a, n)

#Part 3
books = ["Buick '86", 'The Outsider', "Black Monarch"]
print(books)
print(books[0])
books.append('The Count of Monte Cristo')
books.pop(2)
for i in books():
    print(i + " is one of my favorite books")
 
#Part 4
num1 = float(input("Please enter a number\n"))
num2 = float(input("Please enter another number\n"))
num3 = float(input("Please enter a thrid number\n"))
avg = (num1 + num2 + num3) / 3
print(f"{avg} is the average of {num1}, {num2}, and {num3}")