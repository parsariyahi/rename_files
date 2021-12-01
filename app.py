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
            R.switch_places(file, file_path, EXTENSIONS, FORMAT_PATTERN, SEPERATOR)


