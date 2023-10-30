#Lab 2

#Part 1
print("Welcome to the UAlbany offical letter grade-to-number grade conversion program!") # Introduces the program
con = str.lower(input("Do you have the letter grade or number grade?\nInput letter for letter to number\nInput number for number to letter\n")) #Asks if the user has the letter or wants the letter
if con == 'letter': # checks which one they want
    letter = str.lower(input("Please enter the letter grade you recieved\n")) # Accepts the users letter grade and autoformats it into lower case
    if letter == 'a': # Is the letter grade given an a?
        print("An A can represent anything from a 90% to 100% ") # Display the values assoicated
    elif letter == "b": # Is the letter grade given a b?
        print("A B can represent anything from an 80% to 89.9%")
    elif letter == 'c': # Is the letter grade given a c"
        print("A C can represent anything from a 70% to 79.9%")
    elif letter == 'd': # Is the letter grade given a d?
        print("A D can represent anything from a 60% to 69.9%")
    elif letter == "e": # Is the letter grade given an e?
        print("An E can represent anyhting from a 50% to 59.9%")
    elif letter == "f": # Is the letter grade given an f?
        print("A f can represent anything from a 0% to a 49.9%")
    else: # Do this since the letter given is not one of the ones above
        print("Plese input a valid letter grade (A - F)")
else:
    num = int(input("Enter the number grade you recieved\n")) # Accepts the users number grade as an Integer
    if num in range(90, 100): # Checks if the number grade falls anywhere between the two given values
        print("You got an A") # Returns associated letter grade
    elif num in range(80, 89): 
        print("You got a B")
    elif num in range(70, 79):
        print("You got a C")
    elif num in range(60, 69):
        print("You got a D")
    elif num in range(0, 59):
        print("You got an F")
    else: # Only comes here if user inputs something outside the bounds of 0 and 100
        print("Please enter a valid number grade") # Returns a basic error message asking to use a proper value between 0 and 100

#Part 2
print("Welcome to the Even-Odd indentifier program") # Welcomes the user to the program
num = float(input("Please enter any number\n")) # Accepts any number a user provides
if num % 2 == 0: # Checks to see if the remainder of the input number divided by 2 is 0
    print("\n" + str(num) + " is an even number")
else: 
    print("\n" + str(num) + " is an odd number")

#Part 3
number = int(input("Enter 4 numbers\n")) # Allows user to define the first, and therefore largest, value
for x in range(0,3): # runs 3 more times
    num = int(input("")) # asks user for a new number
    if num > number: # Is the value larger than the current largest number
        number = num # Then set the new value as the largest

print(str(number) + " is the largest out of the 4 given numbers") # Display the largest val

#Part 4
print("Enter the length of each side of the triangle") # 
s1 = float(input())
s2 = float(input())
s3 = float(input())
if s1 == s2 and s2 == s3 and s1 == s3:
    print("The given sides indicate the triangle is an Equilateral Triangle")
elif (s1 != s2 and s1 == s3) or (s2 != s3 and s2 == s1):
    print("The given sides indicate the triangle is an Isosceles Triangle")
else:
    print("The given sides indicate the triangle is a Scalene Triangle")

#Part 5
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Deleware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illnois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousisana', 'Maine', 'Maryland', 'Massachusettes', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Wisconsin', 'Wyoming']
capitals = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Agusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul', 'Jakson', 'Jefferson', 'Helena', 'Lincoln', 'Carson', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']
x = 0
while x <= 49:
    print(states[x] + ", " + capitals[x] + ".")
    x += 1
