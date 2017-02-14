#coding=utf-8
import urllib
import re

def getHtml(url):
		page = urllib.urlopen(url)
		html = page.read()
		return html

def getImg(html):
		#reg = r"<img src='(.*?)' alt"
		#imgre = re.compile(reg)
		#imglist = re.findall(imgre,html)
		#imglist = re.findall("<img src='(.*?)' alt",html)
		imglist = re.findall("img data-original='(.*?)' src",html)
		x=0
		for imgurl in imglist:
				print "url: %s" % imgurl
				urllib.urlretrieve(imgurl,'%s.jpg' % x)
				x += 1
		print "x: %d" % x

html = getHtml("http://search.dangdang.com/?key=python&act=input")

#print html
print getImg(html)