import sys
import os
from database import DB


   
#option for user to choose query menu or user data menu
def usersMenuOption():
    print(" Welcome User. Please choose from below: ")
    print("################################")
    print(" (1) User Query menu")
    print("")
    print(" (2) User Information Menu")
    print("")
    print(" (3) Main menu")
    print("")
    print(" (4) Exit the program")
    print("####################################")
    choice2 =  int(input("> "))
    
    if (choice2 == 1):
        print(" User Query Menu...")
        #userMenu()
        DB().isTableCreated()
        #import usermenu
       
    elif (choice2 == 2): 
        print(" User Information Menu")
        #userInformationOption()
        import userinformationoption
        
    elif (choice2 == 3): 
        print(" Main Menu")
        #mainMenu()
        import userchoice
      
    elif (choice2 == 4): 
        print(" Exit Program")
        #exitProgram()
        import exitprogram
        
    elif ((choice2 != 1 or choice2 != 2 or choice2 != 3 or choice2 != 4)): 
        print(" Not a valid choice, please try again!!!")
        
        
usersMenuOption()
        
