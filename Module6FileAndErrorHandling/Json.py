import json

# json.load(JSONfile)
# json.loads(JSON String)
# json.dumps(dictionary) # converts dict -> jsonString
# json.dump(dict, file)


# with open('data.json', 'r') as file:
#     data = file.read()
#     d = json.loads(data)
#     print(d)

d = {
    'name': 'Aniket',
    'marks': 90, 
    'subjects': ['eng', 'maths']
    }

string = json.dumps(d)

with open("data2.json", "w") as file:
    json.dump(d, file)
