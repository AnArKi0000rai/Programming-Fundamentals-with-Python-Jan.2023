first_num = int(input())
sec_num = int(input())

n = sec_num

while n % first_num != 0:
    n -= 1

print(n)