import os
import string

def rename_files():

    file_list=os.listdir("/Users/xiangormirko/Desktop/prank")
    print(file_list)

    saved_path= os.getcwd()
    print("Current Working Directory is "+ saved_path)
    os.chdir("/Users/xiangormirko/Desktop/prank")

    for file_name in file_list:
        print ("Old Name - "+file_name)
        print ("New Nmae - "+file_name.strip("0123456789"))
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)

rename_files()
