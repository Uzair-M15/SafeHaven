from kivy.uix.filechooser import Screen
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class LoginScreen(Screen):
    username = ObjectProperty(None)
    firstName = ObjectProperty(None)
    lastName = ObjectProperty(None)
    password = ObjectProperty(None)