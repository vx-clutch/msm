# Imports
import os
import subprocess
import toml

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class Server:
    def __init__(self, name, path, modLoader, mods):
        self.name = name
        self.path = path
        self.modLoader = modLoader
        self.mods = mods

class Msm(App):
    

if __name__ == "__main__":
    app = Msm()
    app.run()
