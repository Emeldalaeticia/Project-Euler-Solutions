def sum_even_fibonacci(n):
    a, b = 1, 2
    total_sum = 0

    while a <= n:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b

    return total_sum


n = 4000000  # Replace with your desired value
result = sum_even_fibonacci(n)
print(result)
