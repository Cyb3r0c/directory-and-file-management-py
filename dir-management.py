import os

#colors----------------------------------------
class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


#Directory location-------------------------------

#The user will have the chance to chage the CWD prior doing any changes.

def location(path):
    while True:
        local = os.getcwd()
        print(colors.BOLD + local + colors.ENDC)
        path = input("Please, provide the path to any directory:")
        path_exist =  os.path.exists(path)

        if path_exist is True:
            
            os.chdir(path)
        
            break
        else:
            print("\n",colors.RED +"[x]ERROR","Please, provide a valid path.\n" + colors.ENDC, colors.GREEN +"[!]You can do copy paste from the path from above.\n"+ colors.ENDC)
    return

#Creates the directory------------------------------

def create_dir(dir_name, path):
    path = location(path)
    cwd = os.getcwd()
    dir_content = os.listdir(cwd)
    print("\n", colors.BOLD + cwd + colors.ENDC,"\n")
    for items in dir_content:     
        if os.path.isdir(items):                        #Displays the directories in green color.
            print("[! DIR]",colors.GREEN + items + colors.ENDC )
        elif os.path.isfile(items):                      #Displays the files in blue color
            print("[! FILE]",colors.BLUE + items + colors.ENDC)
        else:
            print("[?]",items)
    
    dir_name = input("Enter name of the directory to create:")
    os.mkdir(dir_name)

    print(colors.GREEN + "GREAT SUCCESS " + colors.BOLD + dir_name + colors.ENDC + colors.GREEN + " has been created." + colors.ENDC )
    
    return
    


#Deletes the directory-------------------------------------

def delete_directory(dir_name,path):
    
    path = location(path)
    cwd = os.getcwd()
    dir_content = os.listdir(cwd)
    print("\n", colors.BOLD + cwd + colors.ENDC,"\n")
            
    for items in dir_content:     
        if os.path.isdir(items):                        #Displays the directories in green color.
            print("[! DIR]",colors.GREEN + items + colors.ENDC )
        elif os.path.isfile(items):                      #Displays the files in blue color
            print("[! FILE]",colors.BLUE + items + colors.ENDC)
        else:
            print("[?]",items)
   
    dir_name = input("Enter the directory to delete:")
    while True:
        
        if os.path.isdir(dir_name):
            
            os.rmdir(dir_name)
            print(colors.RED + "\n THE DIRECTORY HAS BEEN REMOVED" + colors.ENDC)
            break
        
        else:
            dir_name = input("[x]ERROR Please, type carefully the directory to delete:")
    
    return
    
#Renames a directory-----------------------------------------

def rename_dir(dir_name,path):
    path = location(path)
    cwd = os.getcwd()
    dir_content = os.listdir(cwd)
    print("\n", colors.BOLD + cwd + colors.ENDC,"\n")
            
    for items in dir_content:     
        if os.path.isdir(items):                        #Displays the directories in green color.
            print("[! DIR]",colors.GREEN + items + colors.ENDC )
        elif os.path.isfile(items):                      #Displays the files in blue color
            print("[! FILE]",colors.BLUE + items + colors.ENDC)
        else:
            print("[?]",items)
   

    while True:
        dir_name = input("Enter the name of the directory to be renamed:")
        dir_renamed = input("Enter the new name for the directory:")
        if os.path.isdir(dir_name):
            
            os.rename(dir_name, dir_renamed)
            print(colors.GREEN + "The directory ",colors.BOLD + dir_name + colors.ENDC,colors.GREEN + " has been renamed to: ",colors.BOLD + dir_renamed, colors.ENDC)
            break
        
        else:
            print(colors.RED + "[x]ERROR Please, select a valid directory:" + colors.ENDC)
            #dir_name = ("ERROR! Please, type carefully the directory to rename:")
    
    
    return
    
    
    
    
    

#MAIN MENU----------------------------------------------
while True:
    print(colors.BOLD + "MENU" + colors.ENDC)

    print(colors.BOLD +"\nPlease, select one of the following options:" + colors.ENDC,
          colors.BLUE + "\n- PRESS [1] TO RENAME A DIRECTORY" + colors.ENDC,
          colors.GREEN + "\n- PRESS [2] CREATE A DIRECTORY" + colors.ENDC,
          colors.RED + "\n- PRESS [3] DELETE A DIRECTORY" + colors.ENDC,
          colors.YELLOW + "\n- PRESS [Q] QUIT" + colors.ENDC)

    path = "Path"
    dir_name = "Directory name"


    choice = input("What option do you choose?")
    
    if choice == "1":
        print(colors.BOLD + "You chose to Rename a directory.\n" + colors.ENDC)
        rename_dir(dir_name,path)
    elif choice == "2":
        print(colors.BOLD + "You chose to Create a directory\n" + colors.ENDC)
        create_dir(dir_name,path)
    elif choice == "3":
        print(colors.BOLD + "You chose to Delete a directory.\n" + colors.ENDC)
        delete_directory(dir_name,path)
    elif choice == "Q" or choice == "q":
        print(colors.BOLD + "Thank you, see you soon!\n\n[!] QUITING...\n" + colors.ENDC)
        break
    else:
        print(colors.BOLD + "Please, select a valid option" + colors.ENDC)




