import yaml
import os
import json
import sys


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
                "Root": {"type": "Root", "params": {}},
                "Sequence": {"type": "Composite", "params": {}},
                "RandomSequence": {"type": "Composite", "params": {}},
                "Selector": {"type": "Composite", "params": {}},
                "RandomSelector": {"type": "Composite", "params": {}},
                "Invert": {"type": "Decorator", "params": {}},
                "Repeat": {"type": "Decorator", "params": {"times": {"type": "float", "des": "重复次数"}}},
                "UntilSuccess": {"type": "Decorator", "params": {}, "des": "直到成功"},
                "UntilFail": {"type": "Decorator", "params": {}, "des": "直到失败"},
            }
    }

    def __init__(self):
        pass

    @staticmethod
    def get_yaml_data(path: str):
        file = open(path, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def save(self, path: str = "config/conf.yaml"):
        file = open(path, 'w', encoding='utf-8')
        yaml.dump(self.data, file)
        file.close()
        self.save_node_params_table()

    def load(self, path: str = "config/conf.yaml"):
        if os.path.isfile(path):
            self.data = self.get_yaml_data(path)
        else:
            self.save(path)

    def save_node_params_table(self):
        path1 = sys.executable
        path2 = os.path.dirname(path1)
        path3 = os.path.dirname(path2) + "\\Assets\\StreamingAssets\\ConfigAsset\\ShareJsonConfig"
        directory_existed = os.path.exists(path3)
        if not directory_existed:
            return
        path = path3+"\\paramsConfig.json"

        table = {}
        for node_name, v in self.data['nodes'].items():
            params = v['params']
            if len(params.keys()) > 0:
                table[node_name] = {}
                for param_name, param_data in params.items():
                    table[node_name][param_name] = param_data.get("default_value")
        data_str = json.dumps(table)
        with open(path, 'w') as f:
            f.write(data_str)
            f.close()
