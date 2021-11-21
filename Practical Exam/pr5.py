def user_pass(password,username="Admin"):
    if password=='123':
        print("You have logged into system")
    else:
        print("Password is incorrect!!!!!!")        
password=input("Enter the password:")
user_pass(password)