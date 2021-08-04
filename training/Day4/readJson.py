
import json

FL = open("books.json", "r")

jsonFile = json.load(FL)

for book in jsonFile['books']:
    for k, v in book.items():
        print(k, " => ", v)
    print("-" * 40)
