import pandas

class DataManager():
    def get_data_csv(self, name):
        df = pandas.read_csv(name, encoding="gbk")
        data = df.values.tolist()
        return data

data_manager = DataManager()
