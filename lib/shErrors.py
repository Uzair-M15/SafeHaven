

class MissingRequiredFile(FileNotFoundError):
    pass

class KeysNotFound(BaseException):
    def __str__(self):
        return "Relevant API keys could not be found"