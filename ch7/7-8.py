sandwich_orders = ['Tuna','Ham','Cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making a {current_sandwich} sandwich...")

    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made....\n" + " ".join(finished_sandwiches))