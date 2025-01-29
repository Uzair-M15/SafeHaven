from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class LoginScreen(Widget):
    username = ObjectProperty(None)
    firstName = ObjectProperty(None)
    lastName = ObjectProperty(None)
    password = ObjectProperty(None)
    context = ObjectProperty(None)