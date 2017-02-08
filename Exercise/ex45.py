class Animal(object):
	def __init__(self,name):
		print "You see a %s" %name
	def action(self):
		pass

class Tiger(Animal):
	def __init__(self,name):
		#self.name = name
		super(Tiger,self).__init__
	def action(self):
		print "The tiger is roaring!"
		
class Lion(Animal):
	def __init__(self,name):
		#self.name = name
		super(Lion,self).__init__
	def action(self):
		print "The Lion is running!"
print "--Welcome to the Jungle adventure--"

print "Which way do you want to go , Left or Right?"

way = raw_input("> ")

if way == "Left":
	tiger = Tiger("tiger")
	#tiger.action()
elif way == "Right":
	lion = Lion("lion")
	#lion.action()
else:
	print "You select a wrong ,you died!!!"