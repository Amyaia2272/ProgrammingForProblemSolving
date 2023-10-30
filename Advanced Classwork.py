"""
entry = {
    "name" : ["Sebastian", "Kevin"],
    "lname" : ["Brand", "Wayne"],
    "email" : ["sbrand@albany.edu", "kevin@thecomputerguy.pro"],
}

repeat = True  

while repeat:
    rep = str.lower(input("Do you wish to create a dicitonary entry? (y/n) "))
    if rep == "n":
        repeat = False
        break
    elif rep == 'y':
        Name = str.title(input("Please enter your first name ONLY: "))
        lName = str.title(input("Please enter your last name ONLY: "))
        email = str.lower(input("Please enter your email address: "))
        entry["name"].append(Name)
        entry['lname'].append(lName)
        entry['email'].append(email)
    else:
        print("Please enter a valid response of either 'y' or 'n' ")


fnames = entry.get("name", [])
lnames = entry.get("lname", [])
emails = entry.get("email", [])

for i in range(len(fnames)):
    print(fnames[i - 1] + " " + lnames[i - 1] + " : " + emails[i - 1])
"""
