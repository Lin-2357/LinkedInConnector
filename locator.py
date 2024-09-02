import pyperclip
import csv


doc = pyperclip.paste()
idx = doc.index("Popular people to follow across LinkedIn")
subdoc = doc[idx:]
ref = 'app-aware-link  discover-entity-type-card__link\" href=\"'
ref2 = 'discover-person-follow-card__occupation t-14 t-black--light t-normal\"'

links = []
for i in range(len(subdoc)-len(ref)):
    if subdoc[i:i+len(ref)] == ref:
        subsubdoc = subdoc[i+len(ref):]
        link = subsubdoc[:subsubdoc.index("\"")]
        occupation = subsubdoc[subsubdoc.index(ref2)+len(ref2):]
        strocc = occupation[:occupation.index("</span>")].replace(">", '').replace("\n", '')
        j = 0
        print(strocc)
        while j < (len(strocc)):
            if strocc[j] != ' ':
                break
            j += 1
        occ = strocc[j:]
        links.append([link, occ])

with open("links.csv", 'w', newline='', errors='ignore') as f:
    fw = csv.writer(f)
    for x in links:
        title = x[1].lower()
        keywords = ['recruit', 'hire', 'hiring', 'manage', 'data', 'analys', 'develop', 'computer', 'engineer', 'information', 'consult', 'software']
        if any([(y in title) for y in keywords]):
            fw.writerow(x)
