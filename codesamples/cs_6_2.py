fpointer = open("mbox-short.txt")
counter = 0;
for line in fpointer :
    line = line.rstrip().lstrip()
    if (not line.startswith("From:") or line.find("@uct.ac.za") == -1) :
        continue;
    counter = counter+1
print "@uct.ac.za : ", counter

        