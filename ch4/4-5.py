lst = range(1,1000001)

print(str(min(lst)) + " " + str(max(lst)))

input("correct?")

a = 0

for i in lst:
    a += i
    print(a)

print(a)