from kivy.uix.accordion import ObjectProperty
from kivy.uix.widget import Widget


class LoginScreen(Widget):
    firstName = ObjectProperty(None)
    lastName = ObjectProperty(None)