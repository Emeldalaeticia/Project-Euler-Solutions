def multiples_of_3_and_5(number):
    total_sum = 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
            
    return total_sum

number = 1000  # Replace with your desired parameter value
result = multiples_of_3_and_5(number)
print(result)
