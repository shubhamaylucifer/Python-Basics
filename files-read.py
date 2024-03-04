file_hnd = open("input.txt","r")

if not file_hnd:
    print('Unable to open the file')

#data = file_hnd.readlines()

data = list(map(lambda x : x.strip('\n'), file_hnd.readlines()))
file_hnd.close()

print(data)

with open("input.txt","r") as file_hnd:
    data = file_hnd.readlines()

print(data)    