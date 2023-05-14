import json
x = open('comments.json')
  
data = json.load(x)
  
for y in data['comments']:
    print(y)

x.close()

# with open("comments.json", mode="r") as j_object:
#    data = json.load(j_object)
#    print(data["karma"])