try:
    fhandler = open("mbox-short.txt", "r")
except IOError:
    print "File 'mbox-short.txt' does not exist"
    quit()

confidence = list()
for line in fhandler:
    line = line.lstrip().rstrip()
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    words = line.split()
    try:
        confidence.append(float(words[1]))
    except ValueError:
        continue

if len(confidence) == 0:
    print "X-DSPAM-Confidence average: 0"
else:
    print "X-DSPAM-Confidence average:", float(sum(confidence) / len(confidence))

fhandler.close()