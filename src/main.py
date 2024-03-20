import modules.servers as server

try:
    server.checkConfigExists()
except:
    print("Unknown error with config")
