from sys import argv

#input two args,script and filename#
script,filename = argv

#open a file#
txt = open(filename)

#print the filename#
print "Here's your file %r:" % filename
#txt read#
print txt.read()
#print text#
print "Type the filename again:"
#input something#
file_again = raw_input(">")
#open the file#
txt_again = open(file_again)
#print the file#
print txt_again.read()