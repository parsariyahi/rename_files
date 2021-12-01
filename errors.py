class Error (Exception) :
    pass


class PatternError (Error) :
    def __init__(self, msg) :
        self.msg = msg

class ExtensionError (Error) :
    def __init__(self, msg, file_ext, valid_ext) :
        self.msg = f"{msg} -- file extension : {file_ext} -- valid extension {valid_ext}"
