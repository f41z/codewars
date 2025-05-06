def square_sum(numbers):
    
    sum_of_squares = 0
    for number in numbers:
       sum_of_squares += number ** 2
    return sum_of_squares
​
numbers = [1, 2, 2]
result = square_sum(numbers)
print(f"The sum of squares for {numbers} is: {result}")