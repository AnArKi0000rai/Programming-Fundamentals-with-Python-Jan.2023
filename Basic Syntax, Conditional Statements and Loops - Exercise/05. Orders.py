number_of_orders = int(input())

total_sum = 0
for order in range(number_of_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if 100.00 >= price >= 0.01 and 31 >= days > 0 and 2000 >= capsules > 0:
        order_sum = (days * capsules) * price
        total_sum += order_sum

        print(f'The price for the coffee is: ${order_sum:.2f}')
print(f'Total: ${total_sum:.2f}')