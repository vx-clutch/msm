import toml
import subprocess
import os

working_dir = os.path.dirname(__file__)
default_config_path = "../../msm.def.toml"
config_path = "../../msm.toml"

def checkConfigExist():
    if not os.path.exists(config_path) or os.stat(config_path).st_size == 0:
        subprocess.run(["cp", default_config_path, config_path])

    with open(config_path, "r") as f:
        config = toml.load(f)

class Server():
    def __init__(self, name):
        self.path = config[name]['path']
        self.Xms = config[name]['Xms']
        self.Xmx = config[name]['Xmx']
    def start():
        subprocess.run([f"cd {path} && ./run.sh"])
