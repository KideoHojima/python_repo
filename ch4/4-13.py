#Five buffet items

buffet = ("fried rice", "shrimp", "bbq", "sausage", "cake")

print("Buffet items include:")
for item in buffet:
    print(item)                     #print each item out

#buffet[1] = "soup"                 #naughty assignment

print("\nThe menu has been changed:")

buffet = ("fried rice", "soup", "bbq", "sunny-side egg", "cake")  
#reassign the variable representing old tuple with a new one

for item in buffet:
    print(item)                     #print each item out