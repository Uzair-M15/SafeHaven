import os
from kivy.app import App
from kivy.uix.widget import Widget
import Login

class SafeHavenApp(App):
    def build(self):
        if os.path.isfile("session/user.json"):
            pass
        else:
            return Login.LoginScreen()

if __name__ == '__main__':
    SafeHavenApp().run()