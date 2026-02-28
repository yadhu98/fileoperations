def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1

for num in count_up_to(3):
    print(num)