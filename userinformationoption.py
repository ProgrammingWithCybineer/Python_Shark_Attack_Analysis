import sys
import os




#Update/ change User name and/or userpassword
def userInformationOption():
    
    print("")
    print("################################")
    print(" (1) Update User Name ")
    print("")
    print(" (2) Update User Password")
    print("")
    print(" (3) Previous Menu ")
    print("")
    print(" (0) Exit the program ")
    print("")
    print("#################################")
    print("")
    choice2 =  int(input("> "))
    
    if (choice2 == 1):
        import updateusername
        

    elif (choice2 == 2):
        import updateuserpassword
        

    elif (choice2 == 3):
        import userchoice
        

    elif (choice2 == 0):
        import exitprogram
        
    
    elif (( choice2 != 0 or choice2 != 1 or choice2 != 2 or choice2 != 3)): 
        print(" Not a valid choice, please try again!!!")
        import userchoice
        
        
        
userInformationOption()
 