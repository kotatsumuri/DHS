import json

def read(jsonfile):
    r=open(jsonfile,"r")
    dic=json.load(r)
    return str(dic["name"])
