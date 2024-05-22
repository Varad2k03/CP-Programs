def fibonacci(n):
    a, b = 0, 1
    fib_list = []
    while b < n:
        fib_list.append(b)
        a, b = b, a + b
    return fib_list

def count_fibonacci_in_range(f, s, fib_list):
    count = 0
    for num in fib_list:
        if f <= num < s:
            count += 1
    return count

fib_list = fibonacci(10**100)

while True:
    f, s = map(int, input().split())
    if f == 0 and s == 0:
        break
    count = count_fibonacci_in_range(f, s, fib_list)
    print(count)


#"INPUT"
#10 100
#1234567890 9876543210
#0 0
#"OUTPUT"
#5
#4