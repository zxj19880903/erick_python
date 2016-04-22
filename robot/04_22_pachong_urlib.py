'''import urllib2

request = urllib2.Request("https://www.1qianbao.com")
response = urllib2.urlopen(request)
print response.read()
'''
'''
import urllib
import urllib2

values = {"username" : "zhaoxinjiang2012@163.com", "password" : "#######"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
'''
'''
import urllib
import  urllib2
values = {}
values['username'] = "zhaoxinjiang2012@163.com"
values['password'] = "######"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2 .urlopen(request)
print response.read()
'''
import urllib
import urllib2
values = {}
values['username'] = "zhaoxinjiang2012@163.com"
values['password'] = "######"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" +data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print  geturl