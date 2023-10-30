import re 

np = r"(\b[a-zA-Z]+\b) (\b[a-zA-Z]+\b)"
ep = r"(\b[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b)"
ap = r"(\d{2}) years old"

name_list = []
email_list = []
age_list = []


while True:
    name = str.strip(str.title(input("Please enter your first and last name"))) 
    #Corrects user input in the event of blank spaces on either end of input (ie "    John Hammond     " -> "John Hammond")
    email = str.strip(str(input("Please enter your email address: ")))
    age = input("Please enter your age: ")
    
    if age.isdigit(): #Checks to make sure the user has input a number (ie "19" -> True, while "m18" -> False)
        nm = re.search(np, name) #name_match
        em = re.search(ep, email) #email_match
        am = re.search(ap, age) #age_match
        
        # Checks if the match returned true AND the user's name is NOT in the user index
        if nm and name not in name_list: 
            fulname = nm.group()
            name_list.append(name)
        # Chekcs if the match returned true AND the user's name IS in the user index
        elif nm and name in name_list:
            print("User already exists")
            quit
        # Comes to the else statement in the event that the match returned False and if the user doesn't exits in the index
        else:
            fulname = "Name not found"
        
        # Checks if the match returned True AND the user's email is NOT in the user index
        if em and email not in email_list:
            emails = em.group()
            email_list.append(email)
        # Checks if the match returned True AND the user's email IS in the user index
        elif em and email in email_list:
            print("Email already exists in system")
            quit
        else:
            emails = 'Email not foumd'
        
        if am and age >= 18:
            Age = am.group()
            age_list.append(age)
        elif am and age < 18:
            print("You must be atleast 18 years old in order to register")
            quit
        else:
            Age = "Age not Found"
        break
    else:
        print("Please only enter numbers for your age")
print("Name: ", name)
print("Email: ", email)
print("Age: ", str(age))