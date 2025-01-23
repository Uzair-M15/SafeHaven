# Abstractions for supabase calls and requests

import os
from lib import shErrors
import json
from supabase import create_client , Client
import geocoder

def checkKeys():
    """Checks for the presence of the api key in SafeHave/keys.json. If api keys are present return true"""
    if os.path.isfile("session/keys.json"):
        try:
            file = open("session/keys.json")
            keys = json.load(file)
            file.close()
            
            if not(keys["tomtom"] == "") and not(keys["supabase"] == ""):
                return True
            return False
        except BaseException as e:
            return False
    else:
        return False

def getkeys():
    if checkKeys():
        file = open("session/keys.json")
        keys = json.load(file)
        file.close()
        return keys
    else:
        raise shErrors.KeysNotFound()

class Manager:
    """Abstraction object for making supabase calls and requests"""
    def __init__(self):
        self.keys = getkeys()
        
        #Initialise supabase client
        self.urls = json.load(open("session/keys.json"))
        self.supabase: Client = create_client(self.urls["supabase"] , self.keys["supabase"])

        