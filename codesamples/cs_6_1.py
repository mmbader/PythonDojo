fpointer = open("mbox-short.txt")
for line in fpointer :
    line = line.rstrip().lstrip()
    if (not line.startswith("From:")) :
        continue;
    print line
        