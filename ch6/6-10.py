people = [ 'john', 'rick', 'mike', 'peter']
numbers = [['1','2','3'],['1','2'],['1','4'],['3','6','7']]

favorite_numbers = {}
for key, person in enumerate(people):
    favorite_numbers[person] = numbers[key]

[print(f"{','.join(value)} is/are {name}'s favorite number.") for name, value in favorite_numbers.items()]

#git