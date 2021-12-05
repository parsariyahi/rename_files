import os
import re
import string
import random
from errors import *

class Rename (AllErrors):
    __path = ''
    __pattern = ''
    __extensions = []
    __ignore_ext = False

    def ignore_extension (self) -> None:
        self.__ignore_ext = True

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

    def get_files_name (self) : # get all file name are in the current dir
        # dir[0] --> dir name ---------- dir[1] --> dirs name in the current dir ---------- dir[2] --> fiels name in the current dir 
        for dir in os.walk(self.__path):
            if dir[2] : #if there is any file
                if not dir[0].startswith('./.') : #ignore .files
                    yield dir[0], dir[2]
    
          
    def check_file_pattern(self, file_name : str) -> bool: #check file pattern with regex
        if re.match(self.__pattern, file_name) : #check file name format for renaming
            return True
        
        else :
            raise FilePatternError("file name and Pattern are not match!!!")
        #TODO raise an error for (file name in not match with pattern)
    
    
    def check_file_ext(self, file_ext : str) -> bool: #check the extension of the file
        if file_ext in self.__extensions :
            return True
        else :
            raise FileExtensionError("File Extension Is Not Valid !!!")
        #TODO raise an error for (file ext is not valid)
    
    #TODO use reges instead of "os" library
    
    def split_file_name_ext(self, file) : # split file name and extention
        file_name, file_ext = os.path.splitext(file)
        
        return file_name, file_ext

    def file_validation (self, file) :
        file_name, file_ext = self.split_file_name_ext(file)

        try :
            if not self.__ignore_ext : 
                self.check_file_ext(file_ext)

            self.check_file_pattern(file_name)

            return True

        except FilePatternError as FPE:
            FPE.args = (FPE.args[0] + " -- file name : " + file_name, )
            raise 

        except FileExtensionError as FEE:
            valid_ext = " | ".join(str(ext) for ext in self.__extensions)
            print(valid_ext)
            FEE.args = (FEE.args[0] + " -- file extension : " + file_ext + " -- valid extension :" + valid_ext, )
            raise


    
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
