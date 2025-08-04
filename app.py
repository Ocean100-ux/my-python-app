import os

def vulnerable():
    user_input = input("Enter something: ")
    os.system(user_input)  # 💣 This is vulnerable to Command Injection

vulnerable()
