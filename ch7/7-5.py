price = ['Free', 10, 15]

while True:
    ui = input('Enter your age: ')
    if ui == '' or ui == 'quit':
        print("Exitting program..")
        break
    ui = max(0, int(ui))
    if ui < 3:
        ui = 0
    elif ui < 13:
        ui = 1
    else:
        ui = 2
    print(f"Your ticket price is {price[ui]}")