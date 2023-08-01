import sys
import os

input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print("Input file does not exist.")
    sys.exit(1)
output_folder_name = sys.argv[2]

file = open(input_file, encoding="utf=8")

read = file.read()
file.seek(0)

line = 1
for word in read:
    if word == '\n':
        line += 1

arr = []
for i in range(line):
    arr.append(file.readline())

sl = ""
dis_str = ""
l = []
c = 1
for x in arr:
    if "#" in x:
        dis_str += x[1:]
        c = 1
        l.append(sl)
        sl = ""

    if c <= 11:
        sl += x
        c += 1

l.append(sl)

it = 1
for i in range(1, len(l)):
    file = open(output_folder_name+"/"+str(it), "w", encoding="utf=8")
    it += 1
    l[i] = l[i].strip()
    while l[i].startswith('"'):
       l[i] = l[i][1:]
    while l[i].endswith('"'):
        l[i] = l[i][:-1]
    file.write(l[i])

print("USRs generated successfully")
