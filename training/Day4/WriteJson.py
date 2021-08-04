
import json

player = {
    "players" :[
        {
            "id": "P001",
            "name" : "Sachin Tendulkar",
            "matches": 560,
            "runs": 24800,
            "age": 38
        },
        {
            "id": "P002",
            "name": "Rahul Dravid",
            "matches": 385,
            "runs": 21200,
            "age": 36
        },
        {
            "id": "P003",
            "name": "Sourav Ganguly",
            "matches": 327,
            "runs": 19500,
            "age": 37
        }
    ]
}

jsonObj = json.dumps(player, indent=4)

print(jsonObj)

FW = open("player.json", "w")

json.dump(player, FW, indent=4)

FW.close()
