from core.config import Config
import json

config: Config = None

need_save = False

def init():
    global config
    config = Config()
    config.load()

def save_config():
    # global config    
    config.save()

def save_file(nodes,file_name):
    data = []
    for k,v in nodes.items():
        # paramStr = json.dumps(v.params)
        data.append({"guid": k ,"name": v.name, "x": v.x(), "y": v.y(), "children": v.child_GUIDS, "parent": v.parent_GUID
                    #  ,"paramStr": paramStr
                     ,"param_values": v.params})
    bin = json.dumps(data, indent=4)
    with open(file_name,'w') as f:
        f.write(bin)
        f.close()