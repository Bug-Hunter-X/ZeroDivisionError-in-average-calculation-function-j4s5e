def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0  # Or raise an exception, depending on requirements
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")  #Output: The average is: 0

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"The average is: {result}") #Output:The average is: 3.0