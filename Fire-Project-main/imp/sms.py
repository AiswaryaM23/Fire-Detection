import urllib.request
import http.cookiejar
username = "9496833638"
passwd = "fire"
#Logging into the SMS Site
url ̇for ̇wsms = 'http://site24.way2sms.com/Login1.action?'
data ̇for ̇wsms = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
data ̇for ̇wsms = data ̇for ̇wsms.encode('UTF-8')
For Cookies:
cookie ̇jar = http.cookiejar.CookieJar()
cookie ̇opener = urllib.request.build ̇opener(urllib.request.HTTPCookieProcessor(cookie ̇jar))
cookie ̇opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86 ̇64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
try:
user ̇open = cookie ̇opener.open(url ̇for ̇wsms, data ̇for ̇wsms)
except IOError:
print("Error while logging in.")
message = 'FIRE DETECTED'
number = '9496833639'
ssionId = str(cookie ̇jar).split(' ')[1].split(' ')[0]
smsurl = 'http://site24.way2sms.com/smstoss.action?'
smsdata = 'ssaction=ss&Token='+ssionId+'&mobile='+number+'&message='+message+'&msgLen=136'
cookie ̇opener.addheaders = [('Referer','http://site25.way2sms.com/sendSMS?Token='+ssionId)]
smsdata = smsdata.encode('UTF-8')
try:
sentpage = cookie ̇opener.open(smsurl, smsdata)
except IOError:
print("Error while sending message")