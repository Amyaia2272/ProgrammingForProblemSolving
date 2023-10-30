import random

special = ["!", ",", "/", "?", ".", "#", "$", "^", "&", "*", "(", ")", "{", "}", "|", ":", ";", "'", '"', "<", ">", " "]

fname = str.title(input("Please enter your first name: "))
lname = str.title(input("Please enter your last name: "))
sp = random.choice(special)

while True:
    sp_ = random.choice(special)
    if sp_ != sp:
        break

num = int(random.randint(1000, 10000))
ln = len(lname)
UserID = sp_ + fname[0] + fname[2] + str(num % 10) + lname[ln - 1] + lname[ln - 2] + str(num) + sp
print(UserID)