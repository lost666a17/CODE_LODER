import time
import json
import random
import os

red='\033[31m'
green='\033[32m'
yellow= '\033[33m'
blue = '\033[34m'

def shoing_codes():
    with open(r"file.json", "r") as read_file:
        data = json.load(read_file)
    shoer = list(data.keys())
    JOINER = ",\n".join(shoer)
    return f"{red}your codes:\n{JOINER}"

def shoing():
    # global data
    os.system("clear")
    print(shoing_codes())
    print(f"{blue}======================================")
    with open(r"file.json", "r") as read_file:
        data = json.load(read_file)
    try:
        coded = int(input(f"{yellow}your code : "))
        user = str(data[f"code {coded}"]["user_name"])
        password = str(data[f"code {coded}"]["password"])
        text = str(data[f"code {coded}"]["text"])
        print(f"your uaer is {user}")
        print(f"your password is {password}")
        print(f"your entry for this code is {text}")
        time.sleep(10)
    except:
        print(f"{red}There is no such code")
        time.sleep("3")

def Enter_new():
    os.system("clear")
    print(shoing_codes())
    print(f"{blue}======================================")
    with open(r"file.json", "r") as read_file:
        data = json.load(read_file)
    print(f"{yellow}1: ENTER CODE")
    print(f"{yellow}2: RANDOM CODE")
    ch = int(input("chose: "))
    if ch == 1:
        os.system("clear")
        print(shoing_codes())
        print(f"{blue}======================================")
        new_code = int(input(f"{yellow}new code: "))
        new_user = input("new user: ")
        new_password = input("new password: ")
        new_text= input("Write a text for this code: ")
        os.system("clear")
        print(f"your code is {new_code}")
        print(f"your user is {new_user}")
        print(f"your password is {new_password}")
        print(f"your entry for this code is {new_text}")
        saveing = input("save(y or n): ")
        if saveing == "y":
            new_data = data
            new_data[f"code {new_code}"] = {"user_name": new_user, "password": new_password,"text": new_text}

            with open(r"file.json", "w") as write_file:
                json.dump(new_data, write_file)
        elif saveing == "n":
            pass
        else:
            print("y or n , y is yes , n is no")
            
    elif ch == 2:
        os.system("clear")
        print(shoing_codes())
        print(f"{blue}======================================")
        PSL = "123456789"
        pslo = str(PSL)
        JOINER = "".join(random.sample(pslo,5))
        new_code = str(JOINER)
        new_user = input(f"{yellow}new user: ")
        new_password = input("new password: ")
        new_text = input("Write a text for this code: ")
        os.system("clear")
        print(f"your code is {new_code}")
        print(f"your user is {new_user}")
        print(f"your password is {new_password}")
        print(f"your entry for this code is {new_text}")
        saveing = input("save(y or n): ")
        if saveing == "y":
            new_data = data
            new_data[f"code {new_code}"] = {"user_name": new_user, "password": new_password,"text": new_text}

            with open(r"file.json", "w") as write_file:
                json.dump(new_data, write_file)
        elif saveing == "n":
            pass
        else:
            print("y or n , y is yes , n is no")
    else:
        print("1 or 2")
def delete_code():
    os.system("clear")
    print(shoing_codes())
    print(f"{blue}======================================")
    with open(r"file.json", "r") as read_file:
        data = json.load(read_file)
    coded = int(input(f"{yellow}code : "))
    delete_code = input(f"delete code {coded}(y or n): ")
    if delete_code == "y":
        try:
            new_data = data
            del new_data[f"code {coded}"]
            with open(r"file.json", "w") as write_file:
                json.dump(new_data, write_file)
        except:
            print(f"{red}There is no such code")
            time.sleep("3")
    elif delete_code == "n":
        pass
    else:
        print("y or n , y is yes , n is no")


def starter():
    os.system("clear")
    print(shoing_codes())
    print(f"{blue}======================================")
    print(f"{yellow}1: SHOING")
    print("2: ENTER NEW CODE")
    print("3: DELETE CODE")
    kd = int(input("chose: "))
    if kd == 1 :
        shoing()
    elif kd == 2 :
        Enter_new()
    elif kd == 3 :
        delete_code()
    else:
        print("chose 1 or 2")
while True:
    starter()
