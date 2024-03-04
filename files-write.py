data = [
    'First Line',
    'Second Line',
    'Third Line',
    'Fourth Line'
]

file_hnd = open("output.txt","w")

for line in data:
    file_hnd.write(line + "\n")

file_hnd.close()

with open("output2.txt", "w") as file_hnd:
    for line in data:
        print(line + '\n', file=file_hnd, end=(''))