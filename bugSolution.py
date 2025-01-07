def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

#Improved Version
def calculate_average_improved(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

my_numbers = [10,20,30]
average_improved = calculate_average_improved(my_numbers)
print(f"The improved average is: {average_improved}")
