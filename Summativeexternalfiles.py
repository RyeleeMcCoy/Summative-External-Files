#-----------------------------
#Writing files
#Ryelee McCoy
#To show an example for accessing and reading external files such as .txt
#text files that are in the same folder as the python file are easily found
#other text files stored in their own folder will need a path to thier location
#-----------------------------
user_details = {}

#----------------------Functions-------------------------

def create_user():
    name = input("What is your username? ")
    race = input("What is your Race? ")
    weapon = input("What is your choice of weapon? ")
    file = name + "inventory" '.txt'
    save = open(file, 'w')
    save.write("Race,")
    save.write(race + ",")
    save.write("Weapon,")
    save.write(weapon + ",")
    save.write("Health,")
    save.write("100,")
    save.write("Level,")
    save.write("1")
    
def character_scraper():   
    user_name = input("What user would you like to open? ")
    file = user_name + "inventory" '.txt'
    details = open(file, 'r')
    user_profile = details.read().split(',') 
    print(user_profile) 
    item = 0
    while item < (len(user_profile)): 
        user_details[user_profile[item]] = user_profile[item + 1]
        item = item + 2
    details.close() 
    return file 
    
def change_values():
    print("You are at level", user_details["Level"]) 
    print("You fought a creature and won! You leveled up but lost 25 Health")
    print("Your health is now at 75")
    print("--------------------------")
    print("LEVEL UP")
    print("--------------------------")
    print("You are now level 2!")
    user_details["Health"] = "75"
    user_details["Level"] = "1"
    
def save_character(file):     
    with open (file, 'w') as f: 
        for akey in user_details.keys(): 
            f.write(akey + ",")
            f.write((user_details[akey]))
            if akey != "Level":
                f.write(",") 

def main():
    create_user()
    filename = character_scraper()
    input("> ")
    change_values()
    input("> ")
    save_character(filename)

    
main()
    
    