import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
import Login
import Feed

LabelBase.register("Lexend" , '../assets/Lexend/Lexend.ttf')

class SafeHavenApp(App):
    def build(self):
        return Login.LoginScreen()
    
    def ChangeScreens(self , widget_name):
        pass
    
    def radio_button_select(self):
        pass


if __name__ == '__main__':
    SafeHavenApp().run()