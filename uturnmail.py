import email, boto.sqs, sys, time, smtplib, json, re, quopri
from bs4 import BeautifulSoup
from pprint import pprint

def is_email(email):
	return re.match(r'[\w\.-]+@[\w\.-]+', email)

def extract_email(email):
	return re.search(r'[\w\.-]+@[\w\.-]+', email).group(0)

def validate(url):
	return "." in url

msg = email.message_from_file(sys.stdin)
data = {}
data["hash"] = 25252525
data["timestamp"] =  time.strftime("%c")
data["sender"] = extract_email(msg.get_unixfrom())
data["urls"] = []
urls = []

for item in msg.get_payload():
       	soup = BeautifulSoup(item.as_string(False))
	urls.extend(soup.select('a[href]'))

try:
    logFile=open('/mnt/spool/uturnmail/script_logs/uno.txt', 'w')
except Exception, e:
     print "Error: unable to open file ---->" + str(e)

for i in urls:
	if i.string != None and validate(i.string) and not is_email(i.string):	
		data["urls"].append(quopri.decodestring(i.string.encode('utf-8').strip()))

result = json.dumps(data)
logFile.write(result)

del logFile, msg, data, item
#<----------------------------------------------------------------------------->
#Will implement save email to a file first to examine it
#AMAZON SQS
#conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ465WWFWWSIUEKIQ', aws_secret_access_key='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')
#Get the queue
#queue = conn.get_queue('myqueue')
#message = "Time of Python Exec." +  time.strftime("%c") + "\n" + vars(msg)
#<------------------------------------------------------------------------------>

client = smtplib.SMTP('127.0.0.1', 10025)
client.sendmail("sepehr.tah@gmail.com", "sept@uturnmail.com", str(result))
client.quit()
del client
sys.exit(0)

