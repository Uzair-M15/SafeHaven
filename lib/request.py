from kivy.uix.filechooser import error
# Abstractions for supabase calls and requests

import os
from lib import shErrors
import json
from supabase import create_client , Client
from lib import settings
import osmnx
import folium
import webbrowser

def checkKeys():
    """Checks for the presence of the api key in SafeHave/keys.json. If api keys are present return true"""
    if os.path.isfile("session/keys.json"):
        try:
            file = open("session/keys.json")
            keys = json.load(file)
            file.close()
            
            if not(keys["supabase"] == ""):
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

def geturls():
    if os.path.isfile('/session/urls.json'):
        file = open('session/urls.json')
        urls = json.load(file)
        file.close()
        return urls
    
    else:
        raise shErrors.MissingRequiredFile()


class Manager:
    """Abstraction object for making calls and requests"""

    def __init__(self):
        self.keys = getkeys()
        
        #Initialise supabase client
        self.urls = json.load(open("session/urls.json"))
        self.supabase: Client = create_client(self.urls["supabase"] , self.keys["supabase"])
        self.supabase.options.function_client_timeout = 60
        
        #Settings handler
        try :
            self.settings = settings.handler()
        except :
            self.settings = None
        self.osmnx = osmnx

    def create_settings_handler(self):
        if os.path.isfile('session/settings.json'):
            self.settings = settings.handler()


    def gen_map(self , center = None) -> list:
        if center == None:
            try:
                center = self.osmnx.geocode(self.settings.get_field("location"))
                return [1 , folium.Map(location = [center[0] , center[1]] , tiles=self.settings.get_field("map_type") , zoom_start=20)]
            except Exception as e:
                print(e)
                return [0 , 'Your location could not be found']
        else:
            return [1 , folium.Map(location = [center[0] , center[1]] , tiles=self.settings.get_field("map_type") , zoom_start=20)]
        
    def add_marker(self , map , coords = None , address = None , name = ''):
        marker_coords = None
        marker_name = ''

        if coords == None :
            if address == None :
                return
            else :
                marker_coords = self.osmnx.geocode(address)
                if name == '' : 
                    marker_name = address.split(',')[0]
        else:
            marker_coords = coords
            if marker_name == '':
                marker_name = coords.__str__()
        
        folium.Marker(location = [marker_coords[0] , marker_coords[1]] , popup = marker_name).add_to(map)

    def show_map(self):
        webbrowser.open_new_tab('map.html')