from gym import *
import sys
from datetime import datetime
print("*"*110)
print("@aurthor :- Siyarani Patro",
      f"\ndate :- {datetime.now()}")
print("*"*110)
x = User()


while True:
    print("\n")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- Welcome To Fitness GYM +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    print("+="*55)
    print("1. For Super User")
    print("2. For Normal User")
    print("3. For Exit")
    print("+="*55)
    chooise = input("Select Your Chooise :")
    if chooise =="1":
        while True:
            print("-------------------------------------- Welcome to the Super User Functionlity --------------------------------------\n")
            print("*"*50)
            print("1.       Add New Member")
            print("2.       View the Members")
            print("3.       Delete added Member")
            print("4.       Update Member Details")
            print("5.       Add New Regeme")
            print("6.       View Regeme")
            print("7.       Update Regeme")
            print("8.       For Exit")
            print("*"*50)

            select = input("Please Select a Chooise :")    
            if select =="1":
                x.Add_member()
            
            if select =="2":
                x.view_member()
                break
            
            if select =="3":
                x.delete_Member()
            
            if select =="4":
                x.update_Member()
            
            if select =="5":
                x.Add_regime()
            
            if select =="6":
                print()
                x.view_regmi()
            
            if select =="7":
                print()
                x.update_regmi()
            
            if select =="8":
                print()
                print("               Thank You          ")
                break
            

    if chooise =="2":
        print("----------------------->>>>>>>>>> Welcome to the User Functionlity <<<<<<<<<---------------------------\n")
        print("*"*50)
        print("1.         View User Profile")
        print("2.         View User Regeme")
        print("3.         For Exit")
        print("*"*50)

        user_select = input("Select Your Chooise :")
        print()
        
        if user_select =="1":
            x.User_Profile()

        if user_select =="2":
            x.user_regime()

        if user_select =="3":
            print("              Thank You          ")
            break   
            
    if chooise =="3":
                print()
                print("              Thank You          ")
                break
