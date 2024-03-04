from json import load,dumps

with open("input.json","r") as json_file:
    data = load(json_file)

print(dumps(data, indent=2))

from json import loads,dump

json_str = '''
{
    "session" : "Python basics",
    "date" : "16th February 2024",
    "mode" : "Webex"
}
'''

json_data = loads(json_str)

print(dumps(json_data, indent=2))

with open("out.json","w") as file_out:
    dump(json_data, file_out,indent=4)
