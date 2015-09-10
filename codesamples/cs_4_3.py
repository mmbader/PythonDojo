while True:
	line = raw_input("> ")
	if line == "done" :
		break
	elif line.startswith("#") :
		continue
	print line
