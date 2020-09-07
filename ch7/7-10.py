poll = {}

while True:
    name = input("(leave blank to end the program) What's your name:")
    if name == '':
        break
    place = input("Where'd you want to go: ")
    poll[name] = place

for name,place in poll.items():
    print(f"{name.title()} would want to go to {place}")