import re

fhandler = open("../data/regex_sum.txt")
result = 0
for line in fhandler:
    result += sum([int(value) for value in re.findall("\d+", line)])
print result
