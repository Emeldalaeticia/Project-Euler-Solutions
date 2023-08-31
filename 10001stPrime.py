def nth_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False

        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6

        return True

    if n == 1:
        return 2

    count = 1
    candidate = 1

    while count < n:
        candidate += 2
        if is_prime(candidate):
            count += 1

    return candidate


print(nth_prime(6)) # Should return 13
print(nth_prime(10)) # Should return 29
print(nth_prime(100)) # Should return 541
print(nth_prime(1000)) # Should return 7919
print(nth_prime(10001)) # Should return 104743
