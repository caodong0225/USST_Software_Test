import json

class DataManager():
    def get_data_json(self, name):
        with open(name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

data_manager = DataManager()
