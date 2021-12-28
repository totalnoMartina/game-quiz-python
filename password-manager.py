master_pwd = input("What is the master password?")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password: ", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

mode = input("Would you like to add a new password, or use existing ones?(view / add) ").lower()
if mode == "view":
    view()
elif mode == "add":
    add()
else:
    print("Invalid mode")