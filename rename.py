import os
import re
import string
import random
from errors import *

class Rename :
    _path = ''
    _pattern = ''

    def get_files_name (self, path) : # get all file name are in the current dir
        # dir[0] --> dir name ---------- dir[1] --> dirs name in the current dir ---------- dir[2] --> fiels name in the current dir 
        for dir in os.walk(path):
            if dir[2] : #if there is any file
                if not dir[0].startswith('./.') : #ignore .files
                    yield dir[0], dir[2]
    
          
    def check_file_pattern(self, file_name : str, pattern : str) : #check file pattern with regex
        if re.match(pattern, file_name) : #check file name format for renaming
            return True
        
        else :
            return None
        #TODO raise an error for (file name in not match with pattern)
    
    
    def check_file_ext(self, file_ext : str, extensions : list) : #check the extension of the file
        if file_ext in extensions :
            return True
        else :
            raise ExtensionError("FILE EXTENSION IS NOT VALID!!!!!", file_ext, extensions)
        #TODO raise an error for (file ext is not valid)
    
    #TODO use reges instead of "os" library
    
    def split_file_name(self, file) : # split file name and extention
        file_name, file_ext = os.path.splitext(file)
        
        return file_name, file_ext
    
    def split_file_format(self, file_name, seperator) : # split our format
        return file_name.split(seperator)
    
    def change_file_name (self, file : str, file_path : str, file_ext : str, new_name : list) :
        try :
            new_file = f"{new_name[1]}-{new_name[0]}{file_ext}" # put new file name and extension together
            
            old_file_path = f"{file_path}/{file}" # create full path for new and old file name
            new_file_path = f"{file_path}/{new_file}"
            os.rename(old_file_path, new_file_path) # rename file with its path
            
            return True

        
        except FileExistsError : #if file exist this will handel it
            letters = string.ascii_lowercase #all letters
            
            rand_str = ''.join(random.choice(letters) for _ in range(3)) #this will create a random string for new file
            new_file = f"{new_name[1]}-{new_name[0]}_{rand_str}{file_ext}"
            
           
            old_file_path = f"{file_path}/{file}"  # create full path for new and old file name
            new_file_path = f"{file_path}/{new_file}"
            os.rename(old_file_path, new_file_path) # rename file with its path
            print(f"{new_file_path=} ---- {old_file_path=}")
            
            return True
        
        return False
    #TODO raise an error for (can not rename this file)

    def switch_places (self, file, file_path, EXTENSIONS, FORMAT_PATTERN, SEPERATOR) :
            file_name, file_ext = self.split_file_name(file) #-------------------------------------------------
                            
            try :
                #TODO make these if in one if with AND -- handel eceptions with raise errors
                if self.check_file_ext(file_ext, EXTENSIONS) :  #-------------------------------------------------
                                
                    if self.check_file_pattern(file_name, FORMAT_PATTERN) :  #-------------------------------------------------
                                
                        rename = self.split_file_format(file_name, SEPERATOR) #-------------------------------------------------
                        self.change_file_name(file, file_path, file_ext, rename)  #-------------------------------------------------
                                
                    else :
                        print(f"{file_path=} {file=}")
                        #TODO do this in a better way
                else :
                    print(f"{file=}")
                    
            #TODO handel with try except and raise error
            except ExtensionError :
                raise
