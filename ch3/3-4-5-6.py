awesome_people = ['John Cena', 'Juan Cena', 'Jose Cena']

print(f"{awesome_people[0]}, {awesome_people[1]}, {awesome_people[2]}, you're invited to my imaginary party, yay!")

absent_guy = 'Jose Cena'
new_guy = 'Juliene Cena'

print(f"Fuck... {absent_guy} can't come, guess I'll invite {new_guy} instead!")

awesome_people[awesome_people.index(absent_guy)] = new_guy

print(f"{awesome_people[0]}, {awesome_people[1]}, {awesome_people[2]}, you're invited to my imaginary party, yay!")

#add 3 more people

awesome_people.insert(0,'Jim Cena')
awesome_people.insert(2,'Jack Cena')
awesome_people.append('Joe Cena')

print(f"{awesome_people[0]}, {awesome_people[1]}, {awesome_people[2]}, {awesome_people[3]}, {awesome_people[4]}, {awesome_people[5]}, you're invited to my imaginary party, yay!\n"
    "Dang it! We only have spaces for 2 imaginary people. Guess they'll have to die, lol\n"
    f"RIP, {awesome_people.pop()}.\nRIP, {awesome_people.pop()}.\nRIP, {awesome_people.pop()}.\nRIP, {awesome_people.pop()}.\n" 
    f"{awesome_people[0]} and {awesome_people[1]}, you're still invited, yay!")

del awesome_people[0], awesome_people[0]

print(f"{awesome_people} still here? Good. ")

