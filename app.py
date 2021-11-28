import os
import re
import string
import random
from rename import Rename
from vals import *

R = Rename()
        
if __name__ == "__main__" :
            
    for file_path, files_name in R.get_files_name(DIR_PATH) :
        for file in files_name :
            file_name, file_ext = R.split_file_name(file) #-------------------------------------------------
                            
            #TODO make these if in one if with AND -- handel eceptions with raise errors
            if R.check_file_ext(file_ext, EXTENSIONS) :  #-------------------------------------------------
                            
                if R.check_file_pattern(file_name, FORMAT_PATTERN) :  #-------------------------------------------------
                            
                    rename = R.split_file_format(file_name, SEPERATOR) #-------------------------------------------------
                    R.change_file_name(file, file_path, file_ext, rename)  #-------------------------------------------------
                            
                else :
                    print(f"{file_path=} {file=}")
            else :
                print(f"{file=}")
                
        #TODO handel with try except and raise error