# beepitett fuggvenyek

napok = ["hetfo", "kedd", "szerda", "csutortok", "pentek"]

for i in range(len(napok)):
    item = napok[i]
    print(item)

# ehelyett inkabb:

for i, item in enumerate(napok):
    print(napok[i])

print(round(3.422312312, 4))

print(sum([3, 4, 5, 5555, 2]))

print(napok.index("kedd"))

# for loop: dictionary
person = {
    "nev": "Anna",
    "kor": 16,
    "address": "Budapest"
}

for key, value in person.items():
    print(key, value)

with open('text.txt', 'r', encoding='utf-8') as inputfile:
    with open('iras.txt', 'w', encoding='utf-8') as outputfile:
        line = inputfile.readline()
        while line:
            outputfile.write(line)
            line = inputfile.readline()
