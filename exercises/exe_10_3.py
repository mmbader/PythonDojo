import urllib
from bs4 import BeautifulSoup

html_doc = urllib.urlopen("http://python-data.dr-chuck.net/comments_208240.html").read()

parsedHtml = BeautifulSoup(html_doc, "html.parser")
tabledata = parsedHtml.find_all("td")

name = None
comments = None
table = list()

for data in tabledata:
    if data.span is not None:
        comments = data.span.string
    elif data.string != "Name" or data.string != "Comments":
        name = data.string

    if name is not None and comments is not None:
        table.append((name, int(comments)))
        name = None
        comments = None

table.sort()

for name, comment in table:
    print "%-15s %d" % (name, comment)
