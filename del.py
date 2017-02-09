import os
#-*-coding:utf-8-*-#
def del_file(path):
	if os.path.isfile(path):
		if path.endswith(".bak"):
			try:
				os.remove(path)
				print "Delete the %s" % path
			except Exception,e:
				print e
	elif os.path.isdir(path):
			for item in os.listdir(path):
				itempath = os.path.join(path,item)
				del_file(itempath)

if __name__ == '__main__':
	dirname = 'E:\\python'
	del_file(dirname)
	