try:
    fhandler = open("mbox-short.txt", "r")
except IOError:
    print "File 'mbox-short.txt' does not exist"
    quit()

emailAddress = dict()
for line in fhandler:
    if not line.startswith("From "):
        continue

    words = line.split()
    key = words[1]
    emailAddress[key] = emailAddress.get(key, 0)+1

fhandler.close()
orderedList = list()
for key, value in emailAddress.items():
    orderedList.append((value, key))

orderedList.sort(reverse=True)
for value, key in orderedList:
    print key, ":", value
