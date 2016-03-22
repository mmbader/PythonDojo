import re

line = "Python is <EM>Awesome</EM>"
result = re.findall("<.+?>", line)
print result
