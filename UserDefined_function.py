def authenticate_login(username, password):
    correct_username = "Rajeeve"
    correct_password = "Python123"

    if username == "" or password == "":
        return "Username and password cannot be empty."

    elif username != correct_username:
        return "Incorrect username."

    elif password != correct_password:
        return "Incorrect password."

    else:
        return "Login successful!"


entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

result = authenticate_login(entered_username, entered_password)
print(result)