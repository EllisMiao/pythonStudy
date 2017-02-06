from sys import argv

script,input_file = argv

#define a fuction print_all
def print_all(f):
	print f.read()
	
#define a fuction rewind
def rewind(f):
	f.seek(0)

#define a fuction print_a_line
def print_a_line(line_count,f):
	print line_count,f.readline()

#open the file
current_file = open(input_file)

#print text
print "First let's print the whole file:\n"

#use the print_all
print_all(current_file)

#print text
print "Now let's rewind,kind of like a tape."

#use th rewind
rewind(current_file)

#print text
print "Let's print three lines:"

#use print_a_line
current_line = 1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)
