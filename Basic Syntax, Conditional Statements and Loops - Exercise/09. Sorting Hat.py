name = input()

student_going = False
while name != 'Welcome!':
    if name == 'Voldemort':
        print('You must not speak of that name!')
        break
    if len(name) < 5:
        house = 'Gryffindor'
        student_going = True
    elif len(name) == 5:
        house = 'Slytherin'
        student_going = True
    elif len(name) == 6:
        house = 'Ravenclaw'
        student_going = True
    elif len(name) > 6:
        house = 'Hufflepuff'
        student_going = True

    if student_going:
        print(f'{name} goes to {house}.')

    name = input()
if name == 'Welcome!':
    print('Welcome to Hogwarts.')

