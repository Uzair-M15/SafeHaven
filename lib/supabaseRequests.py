# Abstractions for supabase calls and requests

import os
from lib import shErrors
import json


def checkKeys():
    """Checks for the presence of the api key in SafeHave/keys.json. If api keys are present return true"""
    if os.path.isfile("keys.json"):
        file = open("keys.json")
        keys = json.load(file)
        
        if keys["here"] == "" and keys["supabase"] == "":
            return False
        
        return True
    else:
        return False


class Requests:
    """Abstraction object for making supabase calls and requests"""
    def __init__(self):
        if checkKeys():
            pass

