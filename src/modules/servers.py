import toml
import subprocess
import os

working_dir = os.path.dirname(__file__)
config_path = os.path.join(working_dir, 'msm.toml')

try:
    with open(config_path, "r") as f:
        config = toml.load(f)
except FileNotFoundError:
    subprocess.run(["cp", "../../msm.def.toml", config_path])
    with open(config_path, "r") as f:
        config = toml.load(f)
if os.stat(config_path).st_size == 0:
    subprocess.run(["cp", "../../msm.def.toml", config_path])
    with open(config_path, "r") as f:
        config = toml.load(f)

class Server():
    def __init__(self):
        self.path = config['path']['path']
        self.Xms = config['ram']['Xms']
        self.Xmx = config['ram']['Xmx']
    def start():
        subprocess.run([f"cd {path} && ./run.sh"])
