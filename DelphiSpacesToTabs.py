import sys



if len(sys.argv) != 2:
    print("USAGE: DelphiSpacesToTabs filename.pas")
    exit(1)

filename = sys.argv[1]
with open(filename) as f:
    contents = f.read()

lines = contents.split('\n')
outputlines = []
for l in lines:
    count = 0
    if len(l) > 0 and l[0] == ' ':
        i = 0
        while l[i] == ' ':
            count += 1
            i += 1
        l = chr(9) * (count // 2) + l[count:]

    outputlines.append(l)


with open(filename, 'w') as f:
    f.writelines('\n'.join(outputlines))


