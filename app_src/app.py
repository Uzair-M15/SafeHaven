from kivy.uix.filechooser import ScreenManager
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
from app_src import Login , Feed
from lib import request , crypt

LabelBase.register("Lexend" , 'assets/Lexend/Lexend.ttf')


class SafeHavenApp(App):
            

    def build(self):
        return Feed.FeedScreen()
        

if __name__ == '__main__':
    SafeHavenApp().run()