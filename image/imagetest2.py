#coding=utf-8
import urllib
import re

def getHtml(url):
		page = urllib.urlopen(url)
		html = page.read()
		return html
		
def getImg(html):
		reg = r'src="(.+?\.jpg)" pic_ext'
		imgre = re.compile(reg)
		imglist = re.findall(imgre,html)
		x=0
		for imgurl in imglist:
				#urllib.urlretrieve(imgurl,'%s.jpg' % x)
				print "url: %s" % imgurl
				x+=1
		print "x: %d" % x

html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)