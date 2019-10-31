#-----------------------------
#Writing files
#Ryelee McCoy
#To show an example for accessing and reading external files such as .txt
#text files that are in the same folder as the python file are easily found
#other text files stored in their own folder will need a path to thier location

#Question: External files are very useful for programming because it makes most things just simpler to organize.
#So for saving data, for example a users saved game data, its much easier to have it on an external file rather then in the program itself.
#it gives it its own file so for multiple users in a game they can have their own file rather then trying to save it on the program itself. 
#Other examples are lists such as for grocery shopping or for items in an inventory its easier to keep it out of the way of the main code. 

#-----------------------------
user_details = {}

#----------------------Functions-------------------------

def create_user():
    name = input("What is your username? ")
    race = input("What is your Race? ")
    weapon = input("What is your choice of weapon? ")
    file = name + "inventory" '.txt' #This creates a name that can be used with a file while using user input.
    save = open(file, 'w')#create the file with the user input, most likely will be their username.
    save.write("Race,")#All of the save.writes are saving the information into the newly created file.
    save.write(race + ",")
    save.write("Weapon,")
    save.write(weapon + ",")
    save.write("Health,")
    save.write("100,")
    save.write("Level,")
    save.write("1")
    
def character_scraper():   
    user_name = input("What user would you like to open? ") #Asks the user for their username to open their file.
    file = user_name + "inventory" '.txt' #This creates a name that can be used with a file while using user input.
    details = open(file, 'r')#Creates the file with the user input, most likely will be their username.
    user_profile = details.read().split(',') #This goes into the file and splits the information between commas to make it into a dictionary.
    print(user_profile) #Prints the newly made dictionary from the file.
    item = 0
    while item < (len(user_profile)): #Whole while statement helps create the information into a useable dictionary.
        user_details[user_profile[item]] = user_profile[item + 1]
        item = item + 2
    details.close() #Closes the file.
    return file #Returns the list needed for later.
    
def change_values():
    print("You are at level", user_details["Level"]) #Brings up what level they are from the previously created dictionary.
    print("You fought a creature and won! You leveled up but lost 25 Health")
    print("Your health is now at 75")
    print("--------------------------")
    print("LEVEL UP")
    print("--------------------------")
    print("You are now level 2!")
    user_details["Health"] = "75"#Changes the stats in the dictionary to save what they did.
    user_details["Level"] = "2"
    
def save_character(file):     #Function: Takes all the information that was changed and what not and saves it back into the file to be used for a later date.
    with open (file, 'w') as f: 
        for akey in user_details.keys(): 
            f.write(akey + ",")
            f.write((user_details[akey]))
            if akey != "Level":
                f.write(",") 

def main():#Calls all the functions to make the program work.
    create_user()
    filename = character_scraper()
    input("> ")
    change_values()
    input("> ")
    save_character(filename)

    
main()
