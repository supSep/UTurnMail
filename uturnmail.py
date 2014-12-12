import email, boto.sqs, sys, time, smtplib
from random import randrange
from pprint import pprint

#raw = sys.stdin.readlines()
#msg = email.message_from_file(''.join(raw))
#msg = sys.stdin.readlines()
#raw = ""
#while True:
#    raw += sys.stdin.readline()
#    if not line:
#       break

msg = email.message_from_file(sys.stdin)
timestamp = "Id: "+  str(randrange(10))+" Time: " + time.strftime("%c")

logFile=open('/mnt/spool/uturnmail/script_logs/uno.txt', 'w')
pprint(vars(msg),logFile)
pprint(timestamp, logFile)

del logFile
del msg 

#<----------------------------------------------------------------------------->
#Will implement save email to a file first to examine it
#AMAZON SQS
#conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ465WWFWWSIUEKIQ', aws_secret_access_key='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')
#Get the queue
#queue = conn.get_queue('myqueue')
#message = "Time of Python Exec." +  time.strftime("%c") + "\n" + vars(msg)
#<------------------------------------------------------------------------------>

client = smtplib.SMTP('127.0.0.1', 10025)
client.sendmail("sepehr.tah@gmail.com", "sept@uturnmail.com", timestamp)
client.quit()

sys.exit(0)
