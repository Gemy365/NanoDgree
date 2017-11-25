import os

def rename_files():
    files_list = os.listdir("/home/gemy/Desktop/nondegree/C1_L1/prank") #List of this Directory
    print(files_list)
    saved_path = os.getcwd()                                    #What Is The Path
    print("Current Working Directory Is: " , saved_path)
    os.chdir("/home/gemy/Desktop/nondegree/C1_L1/prank")        #Change Directory
    for file_name in files_list:
        print("Old Name Is: " , file_name)                      #Old Name File With Numbers
        print("New Name Is: " , file_name.strip("0123456789"))  #New Name Without Numbers
        os.rename(file_name , file_name.strip("0123456789"))    #ReName
    os.chdir(saved_path)                                        #Back To Current Directory
rename_files()
