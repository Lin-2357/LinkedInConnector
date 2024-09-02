from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pyperclip
import csv

# firefoxpath = 'C:/Users/linji/AppData/Roaming/Mozilla/Firefox/Profiles/j5utn2tf.default-release'
# options = webdriver.firefox.options.Options()
# options.add_argument("--profile={}".format(firefoxpath))

# driver = webdriver.Firefox(options=options)

# baselink = 'https://www.linkedin.com/mynetwork/grow/'
# driver.get(baselink)


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