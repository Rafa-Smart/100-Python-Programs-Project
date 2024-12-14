import json
f = open("followers_1.json")
data = json.load(f)
folower = []
for i in data:
    for j in i["string_list_data"]:
        folower.append(j["value"])
f = open("following_1.json")
data = json.load(f)
folowing = []

for i in data["relationships_following"]:
    for j in i["string_list_data"]:
        folowing.append(j["value"])

goodpeople = []
for i in folowing:
    if i in folower:
        goodpeople.append(i)

for i in folowing:
    if i not in goodpeople:
        print("https://www.instagram.com/" + i)