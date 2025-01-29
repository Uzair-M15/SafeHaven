import json

class handler :
    def __init__(self):
        self.settings_path = "session/settings.json"
        file = open(self.settings_path)
        self.properties = json.load(file)
        file.close()

        self.constants = self.properties["constants"]
    
    def set_field(self , field_name , value):
        self.properties[field_name] = value

    def get_field(self , field_name):
        return self.properties[field_name]

    def save(self):
        file = open(self.settings_path , "w")
        new_settings = json.dump(file)
        file.close()
