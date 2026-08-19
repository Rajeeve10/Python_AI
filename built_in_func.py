def calculate_area(length, width):
    area = length * width
    return area


length1 = float(input("Enter the length of rectangle 1: "))  #float buit in func
width1 = float(input("Enter the width of rectangle 1: "))

length2 = float(input("Enter the length of rectangle 2: "))
width2 = float(input("Enter the width of rectangle 2: "))

area1 = calculate_area(length1, width1)
area2 = calculate_area(length2, width2)

total_area = sum([area1, area2])  #sum it in func

print("Area of rectangle 1:", area1)
print("Area of rectangle 2:", area2)
print("Total area:", total_area)