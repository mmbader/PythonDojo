import re

line = "I turn 20 this year"
regexp = re.compile("[0-9]+")
result = regexp.findall(line)

print result