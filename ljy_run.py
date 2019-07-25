'''
 * @Author: lijiayi 
 * @Date: 2019-06-28 11:57:17 
 * @Last Modified by: lijiayi
 * @Last Modified time: 2019-06-28 13:45:54
 '''
#!/usr/bin/python
#-*-coding:utf-8-*-
#python3.7



import ljy_base,ljy_config
import os,sys,time
import traceback
import threading
import json
import random

try:
	os.chdir(os.path.dirname(sys.argv[0]))
except:
	pass

class common():
	def __init__(self,runtimes,username=None,passwd=None,start_time=None,tloop=0,sloop=0):
		#conf
		self.conf=ljy_config.getconf().get_config()
		self.host=self.conf["host"]
		self.origin=self.conf["origin"]
		self.runtimes=int(runtimes)
		self.tloop=int(tloop)
		self.sloop=int(sloop)
		#info
		self.start_time=start_time
		self.username=""
		if username is not None:
			self.username=username
		self.passwd=passwd
		self.token=""
		self.refresh_token=""
		#headers
		self.cookies={}
		self.headers={
		"Accept":"application/json, text/plain, */*",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
		"Content-Type":"application/json;charset=UTF-8",
		"Accept-Encoding":"gzip, deflate",
		"Accept-Language":"zh-CN,zh;q=0.9",
		"Origin": "%s"%(self.origin),
		"Tenant-Id":"%s"%(self.conf["tenantid"])
		}

	# #get token>授权类型password MODE
	# def login(self):
	# 	conf=self.conf
	# 	host=self.host
	# 	uri=host+conf["login"]
	# 	headers=self.headers
	# 	headers["Content-Type"]="application/x-www-form-urlencoded; charset=UTF-8"
	# 	username=self.username
	# 	if self.username is None or self.username=='':
	# 		username=self.getuserlist()[self.runtimes]
	# 		self.username=username
	# 	params={
	# 	"client_id":"%s"%(conf["clientid"]),#应用的appid
	# 	"client_secret":"%s"%(conf["clientsecret"]),
	# 	"grant_type":"password",#授权类型
	# 	"username":"%s"%(self.username),
	# 	"password":"%s"%(conf["passwd"]),
	# 	"check_weak_pwd":"1",
	# 	"version":"01",
	# 	"captchaCode":"%s"%(conf["captchacode"]),
	# 	"captchaText":"bbm7"#验证码
	# 	}
	# 	data={}
	# 	result=ljy_base.base().postHTTP(uri,params=params,data=json.dumps(data),headers=headers,cookies=self.cookies)
	# 	result=ljy_base.base().ResultTextConvert(result)
	# 	try:
	# 		self.token=result["access_token"]
	# 		self.refresh_token=result["refresh_token"]
	# 	except Exception:
	# 		ex=Exception("error；error；error；error；error；error；error；error；'%s':登录失败<%s>"%(username,result))
	# 		raise ex
	# 	return result

	def get_addTeacher_info(self):
		conf=self.conf
		data={"teacher":{
			"userId":"",
			"loginName":"%s"%(self.username),
			"name":"%s"%(self.username),
			"orgId":"%s"%(conf["orgid"]),
			"sex":None,
			"birthday":"",
			"loginMobile":"%s"%(int(conf["teachermobile"])+self.runtimes),
			"jobStatus":"0",#状态
			"extInfo":{
				"GH":"",
				"XM":"%s"%(self.username),
				"YWXM":"",
				"XMPY":"",
				"CYM":"",
				"XBM":"",
				"CSRQ":"",
				"CSDM":"",
				"JG":"",
				"MZM":"",
				"GJDQM":"",
				"SFZJLXM":"",
				"SFZJH":"",
				"SFZJYXQ":"",
				"HYZKM":"",
				"GATQWM":"",
				"ZZMMM":"",
				"JKZKM":"",
				"XYZJM":"",
				"XXM":"",
				"JGH":"",
				"JTZZ":"",
				"XZZ":"",
				"HKSZD":"",
				"HKXZM":"",
				"XLM":"",
				"GZNY":"",
				"LXNY":"",
				"CJNY":"",
				"BZLBM":"",
				"DABH":"",
				"DAWB":"",
				"TXDZ":"",
				"LXDH":"",
				"YZBM":"",
				"DZXX":"",
				"ZYDZ":"",
				"TC":"",
				"GWZYM":"",
				"ZYRKXD":"",
				"teacherType":"%s"%(conf["teachertype"])},
			"staticPassword":"%s"%(conf["staticpasswd"])}}
		return data

	def get_addStudent_info(self):
		conf=self.conf
		data={"student": {
				"loginName": "%s"%(self.username),
				"showPassword": "",
				"name": "%s"%(self.username),
				"status": "0",
				"orgId": "%s"%(conf["orgid"]),
				"classId": "%s"%(conf["classid"]),
				"studentCode": "%s"%(self.username),
				"sex": None,
				"birthday": "",
				"mobilephone": "%s"%(int(conf["studentmobile"])+(int(self.runtimes)-self.tloop)),
				"email": "",
				"userId": "",
				"extInfo": {
					"XH": "",
					"XM": "%s"%(self.username),
					"YWXM": "",
					"XMPY": "",
					"CYM": "",
					"XBM": "",
					"CSRQ": "",
					"CSDM": "",
					"JG": "",
					"MZM": "",
					"GJDQM": "",
					"SFZJLXM": "",
					"SFZJH": "",
					"SFZJYXQ": "",
					"GATQWM": "",
					"ZZMMM": "",
					"JKZKM": "",
					"XYZJM": "",
					"XXM": "",
					"DSZYBZ": "",
					"RXNY": "",
					"NJ": "",
					"BH": "",
					"XSLBM": "",
					"XZZ": "",
					"HKSZD": "",
					"HKXZM": "",
					"SFLDRK": "",
					"TC": "",
					"LXDH": "%s"%(int(conf["studentmobile"])+(int(self.runtimes)-self.tloop)),
					"TXDZ": "",
					"YZBM": "",
					"DZXX": "",
					"ZYDZ": "",
					"XJH": "%s"%(self.username)
				},
				"staticPassword": "%s"%(conf["staticpasswd"])}}
		return data

	def addUser(self):
		conf=self.conf
		host=self.host
		headers=self.headers
		headers["Content-Type"]="application/json;charset=UTF-8"
		headers_add={"Access-Token":"%s"%(self.token)}
		headers.update(headers_add)
		if self.runtimes<self.tloop:
			uri=host+conf["addteacher"]
			self.username=conf["teachernamehead"]+str(self.runtimes)
			data=self.get_addTeacher_info()
		else:
			uri=host+conf["addstudent"]
			self.username=conf["studentnamehead"]+str(int(self.runtimes)-self.tloop)
			data=self.get_addStudent_info()
		result=ljy_base.base().postHTTP(uri,data=json.dumps(data).replace(" ",""),headers=headers)
		result=ljy_base.base().ResultTextConvert(result)
		try:
			return result["serverResult"]
		except:
			return result
	
	def Upload_MultipartFormData(self,file_path):
		conf=self.conf
		host=self.host
		uri=host+"/twasp/fs/fs/file/upload"
		uri=host+conf["upload"]
		file_path=file_path
		headers=self.headers
		headers.pop("Content-Type")
		data={"branchCode":"E000001"}
		#提交files表单固定格式,open(...)部分不能用变量代替：file ={'row_name':(filename,open(file_path,"rb"),'image/jpeg'<-RecContentType)}
		file ={'file':(file_path.split("\\")[-1],open(file_path,"rb"),'application/vnd.ms-excel')}
		# file ={'file':(conf["filename"],open(".\\zero.jpg","rb"),'image/jpeg')}
		result=ljy_base.base().postHTTP(uri,data=data,files=file,headers=headers)
		result=ljy_base.base().ResultTextConvert(result)
		# ljy_base.base().showResult(result)
		file["file"][1].close()
		return result
		#print(result)

	def CustomMethod(self,httpMethod,uri,params=None,data=None,headers_add=None,cookies=None):
		# import pdb
		# pdb.set_trace()
		# print(uri,params,data,headers_add,cookies)
		headers=self.headers
		if params is not None:
			try:
				params=json.loads(params)
			except:
				pass
			params=ljy_base.base()._urlencode(params)
		else:
			params=None
		if data is not None:
			data=data
		else:
			data=""
		if headers_add is not None:
			try:
				headers.update(json.loads(headers_add))
			except:
				pass
		else:
			pass
		if cookies is not None:
			try:
				cookies=json.loads(cookies)
			except:
				pass
		else:
			pass
		if httpMethod=="get":
			result=ljy_base.base().getHTTP(uri,params=params,headers=headers,cookies=cookies)
		else:
			result=ljy_base.base().postHTTP(uri,params=params,data=data,headers=headers,cookies=cookies)
		result=ljy_base.base().ResultTextConvert(result)
		print(result)

	def logout(self):
		conf=self.conf
		host=self.host
		# uri=host+"/openapi-vocationalenroll/login/logout"
		uri=host+conf["logout"]
		headers=self.headers
		result=ljy_base.base().getHTTP(uri,headers=headers)
		return result.headers


	def main(self):
		conf=self.conf
		try:
			self.token=conf["token"]
		except:
			ex=Exception("Token is Null!")
			raise ex
		if conf["custommethod"]=="True":
			self.CustomMethod(httpMethod=conf["httpmethod"],params=conf["params"],uri=conf["uri"],data=conf["data"],headers_add=conf["headers_add"],cookies=conf["cookies"])
		else:
			addresult=self.addUser()
			#self.logout()
			# file_path="C:\\Users\\povti\\Downloads\\导入学生帐号.xls"
			# self.Upload_MultipartFormData(file_path)
		stop_time=time.time()
		print("(%s)总共耗时:{0:.5f}秒>>创建结果(%s)".format(stop_time-self.start_time)%(self.username,addresult))

if __name__ == '__main__':
	c=ljy_config.getconf().get_config()
	try:
		tloop,sloop=c["tloop"],c["sloop"]
		# for i in range(int(c["loop"])):
		if tloop is None or tloop=="":
			tloop=0
		if sloop is None or sloop=="":
			sloop=0
		for i in range(int(tloop)+int(sloop)):
			passwd=c["passwd"]
			username="admin1"
			start_time=time.time()
			a=common(i,username,passwd,start_time,tloop,sloop)
			target=threading.Thread(target=a.main)
			#threading.active_count()线程数量,手动限制每次开启的线程数量
			while threading.active_count()>int(c["thread"]):
				time.sleep(10)
			target.start()
			#threading.Thread.__stop()

	except KeyboardInterrupt:
		print("key break!")
		sys.exit()