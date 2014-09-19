import fileinput #  1
     #  2
for line in fileinput.input(inplace=3): #  3
	line = line.rstrip() #  4
	num = fileinput.lineno() #  5
	print '%-4s # %2i' % (line, num) #  6
