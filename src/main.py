import modules.servers as server

try:
    server.checkConfigExists()
except:
    print("Error verifying msm.toml")
