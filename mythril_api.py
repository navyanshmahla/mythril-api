from fastapi import FastAPI

from mythril_script import *
import json

app = FastAPI()

@app.get('/')
def default():
    return "Server is running! The API is ready"

@app.get("/output/{contract_name}")
async def show(contract_name: str):
    analyze_mythril(contract_name)
    file_json = contract_name.replace(".sol", ".json")
    path_json_final = "./json/"+file_json
    json_file = open(path_json_final, 'r')
    json_data = json_file.read() 
    obj=json.loads(json_data)
    print(str(obj['issues']))