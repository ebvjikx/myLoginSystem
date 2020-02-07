# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:07:12 2020

@author: ebjik
"""

# LOGIN SYSTEM

import csv
import json
  
CSVfile = "usersLS.csv"
JSONfile = "usersLs.json"
file_write = open(CSVfile, "a")
file_read = open(JSONfile, "r").read()
users = json.loads(file_read)

fileWriter = csv.writer(file_write)

def CreateAccount():
    #ask for user info and store info into json & csv file
    Name = input("First, let me know your name!\n").title()
    Age = int(input("Your age too!!\n"))
    checkUname = True
    checkPword = True
    minLength = 6
    
    while checkUname:
        #checks if username already exists
        userName = input("Choose a username.. be creative\n")
        if userName in users:
            print ("\nUsername already exists")
            continue
        else:
            break
    
    while checkPword:
        #checks that password is long enough 
        passWord = input("Choose a password. A strong one.\n")
        if len(passWord) < minLength:
            print("\nPassword must be at least 6 figures long.")
            continue
        else:
            break
        
    #add new user info to csv file
    fileWriter.writerow([Name, Age, userName, passWord])
    
    #add username & password to json file for check when loggin in
    with open(JSONfile) as file:
        file_decoded = json.load(file)
    file_decoded[userName] = passWord
    
    with open(JSONfile, "w") as file:
        json.dump(file_decoded, file)
        
    print ("Account created. Welcome @" + userName)
   
def Login():
    #ask user for login info and verify if user exists and if password is right
    login = True
    
    while login:
        #checks if username and password match and are both correct
        userName = input("Enter your username\n")
        passWord = input("Enter your password\n")
        if userName in users:
            if passWord == users[userName]:
                print ("\nWelcome back @" + userName)
                login = False
            else:
                print ("\nUsername or password incorrect.")
                continue
        else:
            print ("\nUsername or password incorrect.")
            continue
        
def decision():
    #ask the user for what they want to do
    decision = True
    
    while decision:
        decision1 = input("What would you like to do?\n")
        if decision1 == "Create Account":
            CreateAccount()
            decision = False
        elif decision1 == "Login":
            Login()
            decision = False
        elif decision1 == "create account":
            CreateAccount()
            decision = False
        elif decision1 == "login":
            Login()
            decision = False
        else:
            print ("\nNot recognized")
            continue

print ("Welcome Here!")
print ("Create Account")
print ("Login")

decision()


