# Part 1
active_program = ["Typing", "Reading", "Math", "Logical Thinking", "Planning"]

print(active_program[0])

for i in range(0, 3):
    print(active_program[i])
print("\n \n\n")

print(active_program[4])
print(active_program[3])

active_program.append("look at tutorials")
active_program.append("watch movies about programmers")

for i in active_program:
    print(i)
print("\n\n\n")

active_program.append("desire to learn")
active_program.append("commitment to learning")

active_program.remove("watch movies about programmers")

active_program.insert(5, "watch tutorials online")

for i in active_program:
    print(i)
print("\n\n\n")

active_program.remove(active_program[0])
for i in active_program:
    print(i)
print("\n\n\n")

relevant = active_program[1]

active_program.insert(0, relevant)
active_program.pop(2)

sliced = active_program[0:3]

new_list = active_program.copy()

fixed_list = []

for i in range(len(sliced)):
    if new_list[i - 1] == sliced[i - 1]:
        fixed_list.append(new_list[i - 1])
 
if active_program[len(active_program) - 1] == "commitment to learning":
    print("TRUE")
else:
    print("Failure")

#Part 2
length = len(active_program)

m = ["Typing", "Reading", "Math", "Logical Thinking", "Planning"]

for i in range(len(m)):
    print("Every other day, I will practice " + m[i] + " to become a better programmer\n")
    
for x in range(len(m)):
    if x == 3:
        print("Every day, I will practice " + m[:3:] + " in order to become a better programmer\n")

for a in range(len(active_program)):
    print("Every week, I could " + active_program[length - a] + " to become a better programmer")

#Part 3
courseID = [100, 108, 124, 131, 171, 197]
topic = ['Information in the 21st Century', 'Programming for Problem Solving', 'Cybersecurity Basics', 'Introduction to Data Analytics', 'eSports & Digital Gaming Ecosystem', 'Mini Special Topic in Informatics']

SortedID = courseID.sorted()
SortedTopic = topic.sorted()

revID = SortedID.reverse()
revTopic = SortedTopic.reverse()

revsortID = revID.reverse()
revTopic.sort(reverse = True)

for i in range(len(courseID)):
    print(revsortID + "\t\t" + revTopic)

#Part 4
CourseID = (100, 108, 124, 131, 171, 197)
Topic = ('Information in the 21st Century', 'Programming for Problem Solving', 'Cybersecurity Basics', 'Introduction to Data Analytics', 'eSports & Digital Gaming Ecosystem', 'Mini Special Topic in Informatics')

for i in range(len(CourseID)):
    print("Welcome to CINF " + CourseID[i] + ", " + Topic[i])

CourseID.append(200)
Topic.append('Research Methods in Informatics')

CourseID.remove(197)
Topic.remove("Mini Special Topic in Informatics")

for i in range(len(CourseID)):
    print("Welcome to CINF " + CourseID[i] + ", " + Topic[i])
    
#Part 5

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Deleware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illnois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousisana', 'Maine', 'Maryland', 'Massachusettes', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Wisconsin', 'Wyoming']
capitals = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Agusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul', 'Jakson', 'Jefferson', 'Helena', 'Lincoln', 'Carson', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']

#Lines 98 & 99 establishes "states" as a list that contains the names of every state
state_dictionary = dict(zip(states, capitals)) # Compresses States and Capitals into one dictionary and associates each state with its according capital

