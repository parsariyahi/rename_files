class Error (Exception) :
    pass

class FilePatternError (Error) :
    pass

class FileExtensionError (Error) :
    pass


class AllErrors(FileExtensionError, FilePatternError) :
    pass
