import json

result = {
    "success": True,
    "message": "Workflow executed"
}

with open("result.json","w") as f:
    json.dump(result,f,indent=2)
