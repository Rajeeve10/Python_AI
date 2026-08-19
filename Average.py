def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    average = total / len(numbers)

    return average


marks_input = input("Enter your marks separated by spaces: ")

marks = list(map(float, marks_input.split()))

result = calculate_average(marks)

print("Marks:", marks)
print("Average:", result)