with open('table1.yaml', 'r', encoding="utf-8") as f:
    s = f.read()
    lens = (len(s.split("\n")))
strings = s.split("\n")
spc = []
name = []
word = []
xml = '<?xml version="1.0" encoding="UTF-8" ?>\n'
xml += "<root>\n"


def name_class(strr):
    v = ""
    for j in range(len(strr)):
        if strr[j] == " " or strr[j] == "-":
            continue
        elif strr[j] == ":":
            name.append(v)
            return v
        else:
            v += strr[j]


def spc_count(strr):
    strr = strr.replace("-", " ")
    spc.append(len(strr) - len(strr.lstrip(' ')))
    return (len(strr) - len(strr.lstrip(' ')))


def find_words(strr):
    b = 0
    b1 = ""
    for j in range(len(strr)):
        if strr[j] == "'" and b != 0:
            word.append(b1)
            return b1
        elif b == 1:
            b1 += strr[j]
        elif strr[j] == "'":
            b = 1

for i in range(lens):
    a = name_class(strings[i])
    b = spc_count(strings[i])
    c = find_words(strings[i])
    if c == None:
        word.append("")
    print(b, a, c)

maxspc = max(spc)
elem = set(spc)
v = len(elem)
prev = [-1] * maxspc
#print(prev)
#print(("name", name))
#print("spc", spc)
#print(len(word), "word", word)
#print("das'd", lens)

for i in range(lens):
    if spc[i] == maxspc:
        xml += " " * maxspc
        xml += f"<{name[i]}> {word[i]} </{name[i]}>\n"
    else:
        n = prev[spc[i]]
        if n == -1:
            prev[spc[i]] = i
            xml += " " * (spc[i] + 2)
            xml += f"<{name[i]}> {word[i]}\n"
        # print(name[i], word[i],i, "re")
        else:
            xml += " " * (spc[i] + 2)
            xml += f"</{name[n]}>\n"
            xml += " " * spc[i]
            xml += f"<{name[i]}> {word[i]}\n"
            prev[spc[i]] = i
for i in range(len(prev)):
    if prev[3 - i] != -1:
        xml += " " * (spc[prev[3 - i]] + 2)
        xml += f"</{name[prev[3 - i]]}>\n"
xml += "</root>"
print(xml)