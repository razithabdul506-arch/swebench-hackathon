import json

print("Running fake AI agent...")

# fake prompt log
with open("prompts.log", "a") as f:
    f.write(json.dumps({"prompt": "Fix bug"}) + "\n")

# fake agent actions log
with open("agent.log", "a") as f:
    f.write(json.dumps({"action": "generate_patch"}) + "\n")

# fake patch file
with open("changes.patch", "w") as f:
    f.write("dummy patch content")

print("Agent simulation complete")
