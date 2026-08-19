import random


def calculate_area(length, width):
    return length * width


# Generate random measurements for two rectangles
length1 = random.randint(1, 10)    #random m
width1 = random.randint(1, 10)

length2 = random.randint(1, 10)
width2 = random.randint(1, 10)

# Call the user-defined function
area1 = calculate_area(length1, width1)
area2 = calculate_area(length2, width2)

# Use the built-in sum() function
total_area = sum([area1, area2])

print("Rectangle 1 measurements:", length1, "x", width1)
print("Area of rectangle 1:", area1)

print("Rectangle 2 measurements:", length2, "x", width2)
print("Area of rectangle 2:", area2)

print("Total area:", total_area)