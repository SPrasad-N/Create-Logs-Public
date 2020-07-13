
# Program that creates as well as reads files for makng logs.

import datetime

def gettime():
    return datetime.datetime.now()

print("Enter the name of user.")
user_name = input("Enter name:\n")

print("Enter choice as either add or read.")
user_choice = input("Enter choice to do:\n")

print("Enter log-type as food, exercise, etc.")
user_log_type = input("Enter log-type:\n")

def add_log():
    print("Enter what your action as a log.")
    user_log = input("Enter your log:\n")
    with open(f"{user_name.lower()}-{user_log_type.lower()}.txt", "a") as user:
        user.write(str(gettime()) + " : " + str(user_log) +"\n")
        print("Log Entered Successfully !")

def read_log():
    try:
        with open(f"{user_name.lower()}-{user_log_type.lower()}.txt", "r+") as user:
            print(user.read())
            print("Log data read successfully !")
    except:
            print("\nYou don't have such file.\nIf you want to create a new one, enter y otherwise n.")
            continue_create_new_file = input("Wanna create new file? : ")
            if continue_create_new_file == "y":
                with open(f"{user_name.lower()}-{user_log_type.lower()}.txt", "a") as user:
                    print("Enter what your action as a log.")
                    user_log = input("Enter your log:\n")
                    user.write(str(gettime()) + " : " + str(user_log) +"\n")
                    print("Successfully created a new log-file !")
            else:
                print("Exited out of log successfully.\nStart a new trial.")
                exit()

def work_on_log():
    if user_choice == "add":
        add_log()
    elif user_choice == "read":
        read_log()
    else:
        print("Wrong choice !")

work_on_log()

while(True):
    print("Type y to continue or n to exit")
    user_continue = input("Wanna continue? : ")

    if user_continue.lower() == "y":
        print("Enter the name of user.")
        user_name = input("Enter name:\n")

        print("Enter choice as either add or read.")
        user_choice = input("Enter choice to do:\n")

        print("Enter log-type as food, exercise, etc.")
        user_log_type = input("Enter log-type:\n")

        work_on_log()

    else:
        print("Exited out of log successfully !")
        exit()