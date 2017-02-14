import os

def del_file(path):
		if os.path.isfile(path):
			if path.endswith(".jpg"):
				try:
					os.remove(path)
					print "Delete the %s" % path
				except Exception,e:
					print e
		elif os.path.isdir(path):
			for item in os.listdir(path):
				itempath = os.path.join(path,item)
				del_file(itempath)
					
dirname = 'E:\python\image'
del_file(dirname)