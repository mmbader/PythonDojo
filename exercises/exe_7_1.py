try:
    fhandler = open("mbox-short.txt", "r")
except IOError:
    print "File 'mbox-short.txt' does not exist"
    quit()

# days of the week 0  - Monday, 6 - Sunday
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
emailsDay = dict()

for line in fhandler:
    if not line.startswith("From "):
        continue

    words = line.split()
    # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    key = words[2]
    emailsDay[key] = emailsDay.get(key, 0)+1

for day in days:
    print day, ":", emailsDay.get(day, 0)

fhandler.close()
