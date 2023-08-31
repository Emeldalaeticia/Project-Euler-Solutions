def largest_prime_factor(n):
    largest_prime = 2
    
    while n > largest_prime:
        if n % largest_prime == 0:
            n = n // largest_prime
        else:
            largest_prime += 1
    
    return largest_prime



print(largest_prime_factor(600851475143)) # Should return 6857
