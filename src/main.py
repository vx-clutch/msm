# Imports
import os
import subprocess as sub
import toml as t
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()
config_path='../msm.toml'

if os.path.exists(config_path):
    if os.path.getsize(config_path) == 0:
        subprocess.run(["./toml.sh"], shell=True)

with open('../msm.toml', 'r') as f:
    config = t.load(f)

class Server:
    def __init__(self, name, path, modLoader, mods):
        self.name = name
        self.path = path
        self.modLoader = modLoader
        self.mods = mods
print(config)
