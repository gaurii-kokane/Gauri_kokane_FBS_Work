#WAP   
# to prompt user to enter userid and password
correct_id = "admin"
correct_pw = "1234"

for attempt in range(3):
    uid = input("Enter User ID: ")
    pw = input("Enter Password: ")
    if uid == correct_id and pw == correct_pw:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials.")
else:
    print("Too many attempts. Program terminated.")


#while  loop
    correct_id = "admin"
correct_pw = "1234"

attempt = 0
while attempt < 3:
    uid = input("Enter User ID: ")
    pw = input("Enter Password: ")
    if uid == correct_id and pw == correct_pw:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials.")
    attempt += 1
else:
    print("Too many attempts. Program terminated.")

