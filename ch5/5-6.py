age = int(input("Put in your age: "))

if age < 2:
    print("baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("teen")
elif age < 65:
    print("adult")
elif age >= 65:
    print("elder")