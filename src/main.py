from rich.console import Console
from rich.markdown import Markdown

class Server:
    def __init__(self, name, path, modLoader, mods):
        self.name = name
        self.path = path
        self.modLoader = modLoader
        self.mods = mods

server_0 = Server('create', 1, 1, 1)

md = Markdown(MARKDOWN)
console = Console()
console.print(md)
