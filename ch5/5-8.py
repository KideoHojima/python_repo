lst = ['admin', 'john', 'rick', 'mike', 'peter']

if lst:
    for user in lst:
        if user == 'admin':
            print("Hello,admin. Report status.")
        else:
            print(f"Hello, {user}.")
else:
    print("No Data")