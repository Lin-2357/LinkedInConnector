import pyperclip
import csv


doc = pyperclip.paste()
idx = doc.index("Popular people to follow across LinkedIn")
subdoc = doc[idx:]
ref = 'app-aware-link  discover-entity-type-card__link\" href=\"'
ref2 = 'discover-person-follow-card__occupation t-14 t-black--light t-normal\"'
nameref = 'discover-person-follow-card__name t-16 t-black t-bold\">'

links = []
for i in range(len(subdoc)-len(ref)):
    if subdoc[i:i+len(ref)] == ref:
        subsubdoc = subdoc[i+len(ref):]
        link = subsubdoc[:subsubdoc.index("\"")]
        subsubsubdoc = subsubdoc[subsubdoc.index(nameref)+len(nameref):]
        namewsp = subsubsubdoc[:subsubsubdoc.index("</span>")].replace('\n', '')
        occupation = subsubdoc[subsubdoc.index(ref2)+len(ref2):]
        strocc = occupation[:occupation.index("</span>")].replace(">", '').replace("\n", '')
        j = 0
        print(strocc)
        while j < (len(strocc)):
            if strocc[j] != ' ':
                break
            j += 1
        occ = strocc[j:]
        j = 0
        print(namewsp)
        while j < (len(namewsp)):
            if namewsp[j] != ' ':
                break
            j += 1
        name = namewsp[j:]
        links.append([link, occ, name])

with open("links.csv", 'w', newline='', errors='ignore') as f:
    fw = csv.writer(f)
    for x in links:
        title = x[1].lower()
        keywords = ['recruit', 'hire', 'hiring', 'manage', 'data', 'analys', 'develop', 'computer', 'engineer', 'information', 'consult', 'software']
        if any([(y in title) for y in keywords]):
            fw.writerow(x)
