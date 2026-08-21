def calculate_average(numbers): # user method to calculate average 
    if len(numbers) == 0:    #Python built in function to get length of total numbers
        return 0

    total = sum(numbers)   #python built in calculate total marks (sum)
    average = total / len(numbers)  #average to calculate the average marks

    return average


marks_input = input("Enter your marks separated by spaces: ")

marks = list(map(float, marks_input.split())) #this is used to store marks in a list . the split function is used to split any spaces frok the marks input

result = calculate_average(marks) # the list marks is passed to the method and average stored in result

print("Marks:", marks)  # prints marks in list
print("Average:", result)# prints the average