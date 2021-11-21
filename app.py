import os

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
        # split the extention
        file_split = os.path.splitext(file)
        # split month and day
        re_file  = file_split[0].split('-')
        # put new file name and the extension
        re_file = re_file[1] + '-' + re_file[0] + file_split[1]
        # create full path of new and old file name
        full_file_path = f"{file_path}/{file}"
        full_re_file_path = f"{file_path}/{re_file}"
        # rename file with its path
        os.rename(full_file_path, full_re_file_path)


for file_path, file_name in get_file_name('./classes/') :
    rename_file(file_name, file_path)
