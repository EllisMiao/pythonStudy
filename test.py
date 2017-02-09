#-*-coding:utf-8-*-#
import requests
r = requests.get('http://www.wise.xmu.edu.cn/people/faculty')

print r.text