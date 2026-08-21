user_input = input("Enter your age: ")

if not user_input.isdigit():
    print("Invalid input: enter numbers only.")

else:
    age = int(user_input)

    if age < 18:
        print("You are under 18.")

    elif age <= 120:
        print("Valid age: you are an adult.")

    else:
        print("Invalid age: age is too high.")