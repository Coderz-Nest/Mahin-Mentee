#Saving login credentials in a file. Repeadetly ask the user if he wants to create a new login.

# If yes, then ask for website url, username, email, password and save them in a file.
# All the logins must be saved in 1 file.

def create_login():
    website = input("Enter the website URL: ")
    username = input("Enter the username: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    logs=open('create_login.txt','a')
    logs.writelines(f'{website},{username},{email},{password}\n')

    logs.close()

while True:
    login=input("Do you want to create a new login? (yes/no): ")
    if login == "yes":
        create_login()
        print("Logins saved successfully!")
    elif login == "no":
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

