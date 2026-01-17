# Conditions:
# User has 3 attempts
# If correct username & password → login success
# If wrong → tries decrease
# After 3 wrong attempts → account locked

correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("✅ Login Successful!")
        break
    else:
        attempts -= 1
        print("❌ Invalid username or password!")
        print("Remaining attempts:", attempts)

        if attempts == 0:
            print("🔒 Account locked! Too many failed attempts.")
