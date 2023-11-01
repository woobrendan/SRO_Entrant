from fetch_responses import fetch_responses
import json

entries = fetch_responses()

for entry in entries:
    print('entry----', json.dumps(entry, indent=4))
