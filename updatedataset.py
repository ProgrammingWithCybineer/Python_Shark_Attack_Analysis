import sys
import os


#Update the data for user options 
def updateDataset():
    print("")
    print(" Please choose from below ")
    print("############################")
    print(" (1) Update Data")
    print("")
    print(" (2) Return to Admin Menu ")
    print("")
    print(" (3) Exit program ")
    print("#############################")
    print("")
    
    choice3 = int(input("> "))
     
    if (choice3 == 1):
        print(" Updating Data on file ....")
        import sharkattackdata                          
    
    elif (choice3 == 2):
        print("Loading Admin Menu...")
        import adminmenu
    
    elif (choice3 == 3): 
        print("Exiting Program.....")
        import exitprogram

    elif (( choice3 != 1 or choice3 != 2 or choice3 !=3 )):
        print(" Not a valid choice, please try again!!!")
        import adminmenu

        
updateDataset()
    
