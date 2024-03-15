# Imports
import os
import subprocess as sub
import toml
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

with open('../msm.toml', 'r') as f:
    config = toml.load(f)

class Server:
    def __init__(self, name, path, modLoader, mods):
        self.name = name
        self.path = path
        self.modLoader = modLoader
        self.mods = mods
