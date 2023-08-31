def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def largest_palindrome_product(n):
    max_num = 10**n - 1
    min_num = 10**(n - 1)

    largest_palindrome = 0

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome

# Example usage:
print(largest_palindrome_product(2)) # Should return 9009
print(largest_palindrome_product(3)) # Should return 906609
