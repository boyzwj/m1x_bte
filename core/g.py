from core.config import Config
import json

config: Config = None

dirty = False

def init():
    global config
    config = Config()
    config.load("config/conf.yaml")

def set_dirty(dirty=False):
    dirty = dirty
    
def get_dirty():
    return dirty

def save_file(nodes,file_name):
    data = {}
    for k,v in nodes.items():       
        data[k] = {"name": v.name, "x": v.x(), "y": v.y(), "children": v.child_GUIDS, "parent": v.parent_GUID}
    bin = json.dumps(data)
    with open(file_name,'w') as f:
        f.write(bin)
        f.close()