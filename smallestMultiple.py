def gcd(a, b):
    # Calculate the greatest common divisor 
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    # Calculate the least common multiple using the formula: LCM(a, b) = (a * b) / GCD(a, b)
    return (a * b) // gcd(a, b)

def smallest_mult(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result


print(smallest_mult(20)) # Should return 232792560
