sandwich_orders = ['Tuna','pastrami','Ham','pastrami','Cheese','pastrami']

print("The restuarant is out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print('Pastrami removed...')

print("\nSandwiches ordered:\n" + " ".join(sandwich_orders))