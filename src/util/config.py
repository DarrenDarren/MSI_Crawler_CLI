import json
from pathlib import Path
import paths_helper as paths_helper
# import paths_helper.PROJ_PATH as proj_path

class Config:
    
    def __init__(self, name):
        self.name = name
        config_path = paths_helper.CONFIG_PATH / (name + ".json")
        with open(config_path, 'r') as f:
            config = json.load(f)
            
            self.preprocess = config['preprocess']
            self.price_xpath = config["price_xpath"]
            self.in_stock_xpath = config["in_stock_xpath"]
            

    def show(self):
        print(self.name)
        print(self.price_xpath)
        print(self.in_stock_xpath)