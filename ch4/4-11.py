pizzas = ["cheese", "meat", "shrimp","seafood","chicken"]

friend_pizzas = pizzas[:]

pizzas.append("hawaiian")

friend_pizzas.append("pep")

print("my fav pizzas are:")
text = ""
for i in pizzas:
    text += i + ", "
print(text)

print("Her fav pizzas are:")
text = ""
for i in friend_pizzas:
    text += i + ", "
print(text)