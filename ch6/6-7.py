people = [
    {
        'first':'Karen',
        'last': 'Smith',
        'city': 'New York'
    },
    {        
        'first':'Tim',
        'last': 'Jones',
        'city': 'England'
    },
    {        
        'first':'Jeannie',
        'last': 'Lee',
        'city': 'CA'
    }
]

print('\n'.join([' '.join([value.upper() for value in person.values()]) for person in people]))

#[print(' '.join([a.upper() for a in person.values()]) for person in people]