import yaml
import os
class Config():
    data = {
        "last_project": "",
        "node_type": {
            "Root": {},
            "Composite": {},
            "Decorator": {},
            "Condition": {},
            "Action": {}
        },
        "nodes":
            {
                "Root": {"type": "Root","params": {}},
                "Sequence": {"type": "Composite","params": {}},
                "RandomSequence": {"type": "Composite","params": {}},
                "Selector": {"type": "Composite","params": {}},
                "RandomSelector": {"type": "Composite","params": {}},
                "Invert": {"type": "Decorator","params": {}},
                "Print": {"type": "Action","params": {"content":"string"}},
             }
    }

    def __init__(self):
        pass

    @staticmethod
    def get_yaml_data(path: str):
        file = open(path, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data,Loader=yaml.FullLoader)
        return data
    

    def save(self, path: str = "config/conf.yaml"):
        file = open(path,'w',encoding='utf-8')
        yaml.dump(self.data,file)
        file.close()      
        
    def load(self, path: str = "config/conf.yaml"):
        if os.path.isfile(path):
            self.data = self.get_yaml_data(path)
        else:
            self.save(path)
