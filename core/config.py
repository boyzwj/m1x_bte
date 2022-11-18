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
                "HpGreater": {"type": "Condition","params": {"value1":"int" , "value2":"int"}},
                "Print": {"type": "Action","params": {"concent":"string"}},
             }
    }

    def __init__(self):
        self.nodes = None
        self.node_type = None
        self.last_project = None

    @staticmethod
    def get_yaml_data(path: str):
        file = open(path, 'r', encoding="utf-8")
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
