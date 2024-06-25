from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb")  as key_file:
        key_file.write(key)

def load_key():
    with open("key.key","rb") as file:
        key  = file.read()
        return key

key = load_key()
fer = Fernet(key)

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
           data = line.rstrip()
           uname, password = data.split("|")
           print(f"uname: {uname}, password : {fer.decrypt(password.encode()).decode()}")

def add():
    name = input("Account name: ")
    password= input("password: ")
    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode =  input("Would youy like to add a new password or view exixting password? (view/add), press Q to quite ").lower()
    if mode == "q":
        break
    if mode == "view" :
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue 
