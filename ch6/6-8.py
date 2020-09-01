pets = [
    {
        'kind':'dog',
        'name':'Spark',
        'owner':'Jen'
    },
    {
        'kind':'cat',
        'name':'Yuki',
        'owner':'ploy'
    },
    {
        'kind':'turtle',
        'name':'Rick',
        'owner':'Tim'
    }
    ]

[print(f"This {pet['kind']} is called {pet['name'].title()}. They are {pet['owner'].title()}'s!") for pet in pets]