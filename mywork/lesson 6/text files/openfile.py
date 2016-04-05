try:
    fhand = open(raw_input('enter a file name: '))
    
except IOError:
    print 'file not found'
    exit()
    
print fhand