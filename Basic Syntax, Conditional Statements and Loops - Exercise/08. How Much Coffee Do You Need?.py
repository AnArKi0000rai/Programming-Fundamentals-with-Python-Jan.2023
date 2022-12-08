command = input()

count_coffee = 0
while command != 'END':
    if command in('coding', 'dog', 'cat', 'movie'):
        count_coffee += 1
    elif command in('CODING', 'DOG', 'CAT', 'MOVIE'):
        count_coffee += 2

    command = input()

if count_coffee > 5:
    print('You need extra sleep')
else:
    print(count_coffee)