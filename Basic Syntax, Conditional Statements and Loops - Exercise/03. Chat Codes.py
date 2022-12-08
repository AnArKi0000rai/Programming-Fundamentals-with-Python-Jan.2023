number_of_messages = int(input())

for num in range(number_of_messages):
    current_num = int(input())
    if current_num == 88:
        message = 'Hello'
    elif current_num == 86:
        message = "How are you?"
    elif current_num > 88:
        message = "Bye."
    else:
        message = "GREAT!"

    print(message)