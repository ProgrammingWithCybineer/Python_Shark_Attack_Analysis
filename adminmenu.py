

#Admin menu options
def adminMenu():
    print("")
    print(" Welcome Admin. Please choose from below: ")
    print("################################")
    print(" (1) Update dataset ")
    print("")
    print(" (2) Delete a User from the Database")
    print("")
    print(" (3) Exit the program")
    print("####################################")
    choice4 =  int(input("> "))
    
    if (choice4 == 1):
        print(" Update Dataset Menu Loading")
        import updatedataset                            
    
    elif (choice4 == 2) :
        print(" Delete User Menu Loading")
        import deleteuser
    
    elif (choice4 == 3): 
        print(" Exiting Program")
        import exitprogram
        
    
    elif (( choice4 != 1 or choice4 != 2 or choice4 != 3)):
        print(" Not a valid choice, please try again!!!")
        adminMenu()
        
        
adminMenu()