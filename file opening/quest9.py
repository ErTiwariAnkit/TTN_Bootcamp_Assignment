import os
def list_files(dir_path,nasted=True):
        print("files")
        for root,dirs,files in os.walk(dir_path):
                for file in files:
                    if nasted == True:
                        print("-",file)
                    else:
                        for i in files:
                            print(i)
                        exit()

list_files("/home/ankit/bootcamp assign/TTN_Bootcamp_Assignment/file opening/quest/")