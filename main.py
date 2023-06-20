import json
import pandas as pd
file_path = 'result.json'
with open(file_path) as file:
    data = json.load(file)
file_name=data["name"]
print(file_name)
data_csv = []
for i in data["messages"]:
    message_data = {
        "id": i.get("id"),
        "type": i.get("type"),
        "date": i.get("date"),
        "date_unixtime": i.get("date_unixtime"),
        "actor": i.get("actor"),
      "action":i.get("action"),
      "text":i.get("text")
    }
    data_csv.append(message_data)

df = pd.DataFrame(data_csv)
print(df)
# , columns=['id', 'type','date','date_unixtime']