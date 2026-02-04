import json

# fake prompt
prompt = "Fix the failing test"

with open("prompts.log","a") as f:
    f.write(json.dumps({"prompt": prompt})+"\n")

# fake patch
with open("changes.patch","w") as f:
    f.write("dummy patch")

# fake agent log
with open("agent.log","a") as f:
    f.write(json.dumps({"status":"running"})+"\n")
