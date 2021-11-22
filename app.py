import os
import re
import string
import random



# get all file name are in the current dir
def get_file_name (path : str):
    # dir[0] --> dir name
    # dir[1] --> dirs name in the current dir 
    # dir[2] --> fiels name in the current dir 
    for dir in os.walk(path):
        if dir[2] :
            if not dir[0].startswith('./.') :
                yield dir[0], dir[2]
                

def rename_file (files : list, file_path : str) :
    for file in files :
        # split file name and extention 
        file_name, file_ext = os.path.splitext(file)
                        
        #check the extension of the file
        if file_ext in ['.mp4', '.wmv'] :
            #check file pattern with regex
            if re.match(r"(^[0-9]{1,2})-([0-9]{1,2}$)", file_name) :
                # split our format
                rename  = file_name.split('-')
                try :
                    # put new file name and extension together
                    new_file = f"{rename[1]}-{rename[0]}{file_ext}"
                    
                    # create full path for new and old file name
                    old_file_path = f"{file_path}/{file}"
                    new_file_path = f"{file_path}/{new_file}"
                    
                    # rename file with its path
                    os.rename(old_file_path, new_file_path)

                #if file exist this will handel it
                except FileExistsError :
                    #all letters
                    letters = string.ascii_lowercase
                    #if file exist this will create a random string
                    rand_str = ''.join(random.choice(letters) for _ in range(3))
                    new_file = f"{rename[1]}-{rename[0]}_{rand_str}{file_ext}"
                    
                    # create full path for new and old file name
                    old_file_path = f"{file_path}/{file}"
                    new_file_path = f"{file_path}/{new_file}"
                    
                    # rename file with its path
                    os.rename(old_file_path, new_file_path)
                    print(f"{new_file_path=} ---- {old_file_path=}")
            else :
                print(f"{file_path=} {file=}")


if __name__ == "__main__" :    

    for file_path, file_name in get_file_name('./classes/') :
        rename_file(file_name, file_path)