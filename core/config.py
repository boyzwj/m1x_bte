import yaml
import os

class Config():
    data = {
        "last_project": "",
        "node_type": {
            "Root": {"style": "background:#AABBCC;"},
            "Composite": {"style": "background:#FFFFFF;"},
            "Decorator": {"style": "background:#EEC211;"},
            "Condition": {"style": "background:#A25EA2;"},
            "Action": {"style": "background:#33CC8F;"}
        },
        "nodes": []
        }
    def __init__(self):
        pass
    
    def get_yaml_data(self,path: str):
        file = open(path, 'r',encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data)
        return data 
    
    def load(self, path: str):
        if os.path.isfile(path):
            self.data = self.get_yaml_data(path)
        self.last_project = self.data["last_project"]
        self.node_type = self.data["node_type"]
        self.nodes = self.data["nodes"]
            
        
        