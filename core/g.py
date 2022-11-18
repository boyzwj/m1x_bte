from core.config import Config
import json

config: Config = None

need_save = False

def init():
    global config
    config = Config()
    config.load("config/conf.yaml")


def save_file(nodes,file_name):
    data = {}
    for k,v in nodes.items():       
        data[k] = {"name": v.name, "x": v.x(), "y": v.y(), "children": v.child_GUIDS, "parent": v.parent_GUID,"params": v.params}
    bin = json.dumps(data)
    with open(file_name,'w') as f:
        f.write(bin)
        f.close()