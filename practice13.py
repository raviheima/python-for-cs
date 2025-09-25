
USERNAME = "admin"
PASSWORD = "password123"


attempt = 3
while attempt >0:
    admin_int = input("Enter username: ")
    admin_pass = input("Enter password: ")
    if USERNAME == admin_int and PASSWORD == admin_pass:
        print("Access Granted ")
        print("Welcome Admin")
    else:
        print("Access Denied")
        attempt = attempt - 1
print("Maximum attempts exceeded: ")