#ERROR CODES

BAD_REQUEST = 400
UNAUTHORISED = 401
FORBIDDEN = 403
REQUEST_TIMEOUT = 408


class MissingRequiredFile(FileNotFoundError):
    pass

class KeysNotFound(BaseException):
    def __str__(self):
        return "Relevant API keys could not be found"

class error_code:
    def __init__(self , number , message):
        self.number = number
        self.message = message
    
    def __str__(self):
        return '{}:{}'.format(str(self.number) , self.message)