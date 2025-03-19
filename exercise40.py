import json
from pprint import pprint
   
with open("person.json", ) as f:
   data = f.read()


data = json.loads(data)
pprint(data)
print(type(data))