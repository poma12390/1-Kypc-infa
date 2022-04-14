import re
import time

start_time = time.time()

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
    patern = "\w+:"
    v = (re.findall(patern, strr))
    name.append(str(v[0])[:-1])
    return str(v[0])[:-1]


def spc_count(strr):
    strr = re.sub(r"-", r" ", strr)
    v = re.findall(r"^\s+", strr)
    try:
        spc.append(len(v[0]))
        return len(v[0])
    except:
        spc.append(0)
        return 0


def find_words(strr):
    patern = "'[^+]+'"
    name = re.findall(patern, strr)
    if len(name) > 0:
        word.append(str(name[0])[1:-1])
        return str(name[0])[1:-1]
    else:
        return None


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
print(prev)
print(("name", name))
print("spc", spc)
print(len(word), "word", word)
print("das'd", lens)

for i in range(lens):
    if spc[i] == maxspc:
        xml += " " * (maxspc + 2)
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
            xml += " " * (spc[i] + 2)
            xml += f"<{name[i]}> {word[i]}\n"
            prev[spc[i]] = i
for i in range(len(prev)):
    if prev[3 - i] != -1:
        xml += " " * (spc[prev[3 - i]] + 2)
        xml += f"</{name[prev[3 - i]]}>\n"
        print(i)
xml += "</root>"
print(xml)
print('%.5f' % ((time.time() - start_time)*10),"seconds")
