import urllib
from bs4 import BeautifulSoup

html_doc = urllib.urlopen("http://python-data.dr-chuck.net/comments_208240.html").read()

parsedHtml = BeautifulSoup(html_doc, "html.parser")
comments = parsedHtml.find_all("span")
total = 0

print "Total of comments: %d" % sum([int(tag.string) for tag in comments])
