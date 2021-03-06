import os
import re
import string
import random
from errors import *

class Rename :
    __path = ''
    __pattern = ''
    __extensions = []
    __ignore_ext = False
    __ignore_pattern = False
    __ignored_files = []

    
    def ignore_extension (self) -> None:
        self.__ignore_ext = True

    def ignore_pattern (self) -> None:
        self.__ignore_pattern = True

    def set_path (self, path : str) -> None :
        self.__path = path

    def get_path (self) -> str :
        return self.__path

    def set_pattern (self, pattern : str) -> None :
        self.__pattern = pattern

    def get_pattern (self) -> str :
        return self.__pattern

    def set_extension (self, valid_exts : list) :
        self.__extensions.extend(valid_exts)

    def get_extension (self) -> list:
        return self.__extensions
    
    def get_ignored_files(self) :
        
        return self.__ignored_files


    def get_files_info (self) : # get all file name are in the current dir
        # dir[0] --> dir name ---------- dir[1] --> dirs name in the current dir ---------- dir[2] --> fiels name in the current dir 
        for dir in os.walk(self.__path):
            if dir[2] : #if there is any file
                if not dir[0].startswith('./.') : #ignore .files
                    yield dir[0], dir[2]
    
          
    def check_file_pattern(self, file_name : str) -> bool: #check file pattern with regex
        if re.match(self.__pattern, file_name) : #check file name format for renaming
            return True
        
        else :
            raise FilePatternError("file name is not match with your pattern!!!")
    
    
    def check_file_ext(self, file_ext : str) : #check the extension of the file
        if file_ext in self.__extensions :
            return True
        else :
            raise FileExtensionError("File Extension Is Not Valid !!!")
    
    def split_file_name_ext(self, file:str) : # split file name and extention
        file_name, file_ext = os.path.splitext(file)
        
        return file_name, file_ext

    def file_validation (self, file_name:str, file_ext:str) :

        try :
            if not self.__ignore_ext :
                self.check_file_ext(file_ext)
            if not self.__ignore_pattern :
                self.check_file_pattern(file_name)

            return True

        except FilePatternError as FPE:
            FPE.args = (FPE.args[0] + " -- file name : " + file_name, )
            raise
            
        except FileExtensionError as FEE:
            valid_ext = " | ".join(str(ext) for ext in self.__extensions)
            FEE.args = (FEE.args[0] + " -- file extension : " + file_ext + " -- valid extension :" + valid_ext, )
            raise
        
    def split_file_format(self, file_name, seperator) -> str: # split our format
        return file_name.split(seperator)
    
    
    def generate_random_str(self) :
        letters = string.ascii_lowercase #all letters
        rand_str = ''.join(random.choice(letters) for _ in range(3)) #this will create a random string for new file
        
        return rand_str
    
    def change_file_name (self, file:dict) -> bool:
        # file {name : file name , path : file path, new_name : file new name}
        old_file_path = f"{file['path']}/{file['name']}" # create full path for new and old file name
        new_file_path = f"{file['path']}/{file['new_name']}"
        try :
            os.rename(old_file_path, new_file_path) # rename file with its path
            return True
        
        except FileExistsError : #if file exist this will handel it
            rand = self.generate_random_str
            new_file_path = f"{file['path']}/{rand}_{file['new_name']}"

            os.rename(old_file_path, new_file_path) # rename file with its path
            
            return True
        
        return False
    #TODO raise an error for (can not rename this file)

    def switch_places (self, seperator:str) :
        for path, files in self.get_files_info() :
            for file in files :
                file_name , file_ext = self.split_file_name_ext(file)
                self.file_validation(file_name, file_ext)      
                new_file_name = file_name.split(seperator)
                new_file_name = new_file_name[1] + seperator + new_file_name[0] + file_ext
                file_info = {
                        "name" : file,
                        "path" : path,
                        "new_name" : new_file_name
                        }
                self.change_file_name(file_info)

    def numerical_acs(self, **detail) :
        prefix = detail.get('prefix', '')
        suffix = detail.get('suffix', '')
        seperator = detail.get('seperator', '')

        if seperator : 
            prefix = prefix + seperator if prefix else prefix
            suffix = seperator + suffix if suffix else suffix

        root = 1

        for path, files in self.get_files_info() :
            for file in files :
                file_name , file_ext = self.split_file_name_ext(file)
                self.file_validation(file_name, file_ext)      
                new_file_name = prefix + str(root) + suffix + file_ext
                file_info = {
                        "name" : file,
                        "path" : path,
                        "new_name" : new_file_name
                        }
                self.change_file_name(file_info)
                root += 1
