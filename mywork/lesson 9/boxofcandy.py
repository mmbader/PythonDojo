import re

line = "A box of candy costs $20.00"
result = re.findall("\$[0-9.]+", line)
print result