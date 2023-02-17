import datetime
import string
import json
import re
import os


def welcome():
    # Welcome Function
    print("Welcome to our library!\n")
    entry_select = int(input("Enter 1 to login \nEnter 2 to register \nEnter 3 to exit \n\n"))
    if entry_select == 1:
        login()
        print("You have successfully logged in!")
    elif entry_select == 2:
        register()
    elif entry_select == 3:
        print("You have successfully logged out!")
        exit()
    else:
        print("Wrong Entry")

    
def libraryCode():
    library_code = 10000
    library_code += 1
    return library_code


def register():
    first_name = input("please enter your first name: ")
    first_name = string.capwords(first_name)
    last_name = input("please enter your last name: ")
    last_name = string.capwords(last_name)

    while True:
        try:
            national_id = input("please enter your national id number: ")
            if len(national_id) == 10:
                national_id = int(national_id)
                break
            print("Wrong entry!")
        except Exception as e: 
            print(e)

    date_of_birth = input("What is your B'day? (in DD/MM/YYYY) ")  
    date_of_birth = datetime.datetime.strptime(date_of_birth,"%d/%m/%Y").date()  
    print("Your B'day is : "+date_of_birth.strftime('%d/%B/%Y'))
    date_of_birth = date_of_birth.strftime('%d-%m-%Y')
    try:
        address = input("please enter your address: ")
        print(f"Your address is: {address}")   
    except Exception as e: 
            print(e)

    library_code = libraryCode()
    print(f"Your library code is: {library_code}")
    date_of_registeration = datetime.date.today()
    print(f"your date of registration is: {date_of_registeration}")
    date_of_registeration = date_of_registeration.strftime('%d-%m-%Y')

    member = {}
    member['fn'] = first_name
    member['ln'] = last_name
    member['dob'] = date_of_birth
    member['addr'] = address
    member['lc'] = library_code
    member['dor'] = date_of_registeration

    save_it = input("Do you want to save your data? type y for yes: ")
    if(save_it == 'y'):
        save(member)
    else:
        print("Wrong entry, saving data aborted!")


    welcome()




def load():
    with open("members.txt", "r") as dbfile:
        data = dbfile.readlines()
        print(data)
    return data

def login():
    data = load()
    print(data)
    n=0
    for k in data:
        myjson = json.loads(str(k.splitlines())[2:-2])
        print(myjson)
        n+=1
        print(f'{n}: {myjson["fn"]}')

def save(member):
    print("1#" + str(member))
    members_json = json.dumps(member, default=str)

    f = open("members.txt", "a")
    if os.stat("members.txt").st_size != 0:
        f.write("\n")
    f.write(str(members_json))
    f.close()

    print("The data below has been saved successfully!")

def check():
    os.stat("members.txt").st_size == 0