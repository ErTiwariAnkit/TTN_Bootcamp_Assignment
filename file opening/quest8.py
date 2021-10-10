import os
import glob
def rename_all(dir_path,pattern,suffix):
    result=glob.glob(dir_path+pattern)
    for i in result:
        old_name=i
        new_name=os.path.splitext(i)[0]+suffix+".txt"
        os.rename(old_name,new_name)
rename_all("/home/ankit/bootcamp assign/TTN_Bootcamp_Assignment/file opening/","Test_file_*.txt","_renamed")