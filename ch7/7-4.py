flag = True
while flag == True:
    cum = input("Please Type a topping for pizza: \n")
    if cum == 'quit':
        print("Fuck you. I quit.")
        flag = False
    elif cum:
        print(f'{cum} is a shitty pizza topping, but I will add it anyway, fuck you.')
    else:
        print("what..")