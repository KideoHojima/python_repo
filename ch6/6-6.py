favorite_language = {'Sarah':'Python', 'John':'C++', 'Tony':'Java'}

people = ['Sarah','Lee','Jim']

for person in people:
    if person in favorite_language.keys():
        print('Thank you for your response.')
    else:
        print('Please submit your response to the poll')