import random
import json
with open("Workout_regemi.json","r") as f:
    workout_regmi = json.load(f)

class Supper_User:
    def __init__(self): 
        self.member = {}  
        self.key = len(self.member)+1
        global workout_regmi

    def Add_member(self):
        nos = int(input(" Enter How Many Members Your Want to Add : "))
        for i in range(1,nos+1):
            name = input("Enter Name Here : ")
            age = input("Enter Age Here : ")
            gender = input("Enter Gender Here : ")
            phone_num= input("Enter Moible Number Here : ")
            BMI = input("Enter Your BMI Here : ")
            dueration = input("Enter Your Membership Dueration Here : ")
            d = {"Name ": name,"Age ": age,"Gender ": gender,
                "Phone Number":phone_num,"BMI":BMI,"Dueration":dueration}
            self.member[self.key] = d
            print(f"Your {i} Member Got Added\n ")
            self.key = len(self.member)+1
        with open("GYM_Members.json","w") as f:
            json.dump(self.member,f,indent=4)
        return "Your GYM Member Got Added"  


    def view_member(self):
        with open("GYM_Members.json","r") as f:
            temp = json.load(f)
        while True:
            mem_num = input("Enter Your Membership Number :")
            print("*"*55)
            print("--------------->>>>Members Details<<<<--------------")
            if mem_num in temp:
                for i , v in temp[mem_num].items():
                    print(i,":",v)
                print("*"*55)
                print("--------------->>>>Workouts<<<<--------------")
                for j,k in workout_regmi[temp[mem_num]["BMI"]].items():
                    print(j,":",k)
                return ""
            else:
                print()
                print("Enter a Valid Membership Number\n")

    def delete_Member(self):
        with open("GYM_Members.json","r") as f:
            temp = json.load(f)
        while True:                
            del_Id = input("Enter Your Membership Number which You Want to Delete :")
            if del_Id in temp:
                del temp[del_Id]
                with open("GYM_Members.json","w") as f:
                    json.dump(temp,f,indent=4)
                print()
                print("Your Members Got Delete")
                return ''
            else:
                print()
                print("Enter A Valid Membership Number\n")

    def update_Member(self):
        with open("GYM_Members.json","r") as f:
            temp = json.load(f)      
        print("->>")        
        update_Id = input("Enter Your Membership Number which You Want to Update :")
        if update_Id in temp:
            while True:
                print("-------------->>>>Fildes Are <<<<---------")
                for i , v in temp[update_Id].items():
                    print(i,":",v)
                field = input("select Your Field :")
                updated_value = input("Enter Your Updated Value :")
                temp[update_Id][field] = updated_value
                with open("GYM_Members.json","w") as f:
                    json.dump(temp,f,indent=4)
                print()
                print("Your Members Got Update")
                for i , v in temp[update_Id].items():
                    print(i,":",v)
                break
        else:
            print()
            print("Enter A Valid Membership Number\n")

    def Add_regime(self):
        with open("Workout_regemi.json",'r') as f:
            temp =  json.load(f)
        new_regmi = {}
        regmi_id = input("Enter Your Regime ID :")
        if regmi_id in temp:
            return "ID Alreasd exit Try Different ID"
        mon = input("Enter Workout for Monday :")
        tues = input("Enter Workout for Tuesday :")
        wed = input("Enter Workout for Wednesday :")
        thrues = input("Enter Workout for Thruesday :")
        fri = input("Enter Workout for Friday :")
        sat = input("Enter Workout for Saturaday :")
        sun = input("Enter Workout for Sunday :")
        d = {"Monday":mon,"Tuesday":tues,"Webnesday":wed,"Thrusday":thrues,"Friday":fri,"Saturday":sat,"Sunday":sun}
        new_regmi[regmi_id] = d
        print("-------------------->>>>Your Regmi Got Created <<<<------------")
        for i, v in new_regmi.items():
            print(i,":",v)
        temp.update(new_regmi)
        with open("Workout_regemi.json",'w') as f:
            json.dump(temp,f,indent=4)
        return ""
    
    def view_regmi(self):
        while True:
            print("*"*55)
            print("1. View All Regeme ")
            print("2. View Regeme by Membership  ")
            print("*"*55)
            choice = input("select a button :")
            if choice =="1":
                print("+="*15)
                print(f"Press-->>{workout_regmi.keys()} for Regemi ")
                selction = input("Select a Button :")
                if selction in workout_regmi.keys():
                    print("--------------------->>>>>Regeme Details <<<<<<<<<<<<<----------\n")
                    for i , v in workout_regmi[selction].items():
                        print(f"{i} :{v}")
                                
            elif choice =="2":
                mem_num = input("Enter Your Membership Number ")
                with open("GYM_Members.json","r") as f:
                    temp = json.load(f)
                for j,k in workout_regmi[temp[mem_num]["BMI"]].items():
                    print(j,":",k)
                return ""

            else:
                print(" Invalid Selection ")    
                break
    

    def update_regmi(self):
        print(f"Press-->>{workout_regmi.keys()} for Regemi ")
        selction = input("Select a Regemi ID for Updatation  :")        
        print("*"*30)
        for i , v in workout_regmi[selction].items():
                print(f"{i} :{v}")
        print("*"*30)
        field = input("Select Your Day :")
        updated = input("Enter Your Updated Workout :")
        workout_regmi[selction][field] = updated
        with open("Workout_regemi.json",'w') as f:
            json.dump(workout_regmi,f,indent=4)
        return "Your Workout Got Updated"


with open("GYM_Members.json","r") as f:
        temp = json.load(f)


class User(Supper_User):
    def __init__(self):
        super().__init__()
        global temp
    
    def user_regime(self):
        self.ID = input("Enter Your Membership  Id :")
        print("--------------->>>>Workouts<<<<--------------")
        for j,k in workout_regmi[temp[self.ID]["BMI"]].items():
            print(j,":",k)
        return ""
          
    
    def User_Profile(self):
        self.ID = input("Enter Your Membership  Id :")
        print("*"*55)
        print("--------------->>>>Members Details<<<<--------------")
        if self.ID in temp:
            for i , v in temp[self.ID].items():
                print(i,":",v)
            print("*"*55)
            return ""
        else:
            print("ID is Not Avaliable Please First")    

        
  



