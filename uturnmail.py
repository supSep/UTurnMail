import email, boto.sqs, sys, time, smtplib

msg = email.message_from_file(sys.stdin)

from pprint import pprint
logFile=open('/mnt/spool/uturnmail/script_logs/uno.txt', 'w')
pprint(vars(msg),logFile)
pprint("We made it!", logFile)
pprint(time.strftime("%c"), logFile)

#Will implement save email to a file first to examine it

#AMAZON SQS
#conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ465WWFWWSIUEKIQ', aws_secret_access_key='kA8TVCAS8VKafAfS0P0XSIU+iW0IQPJvDs/OKA$

#Get the queue
#queue = conn.get_queue('myqueue')

client = smtplib.SMTP('127.0.0.1', 10027)
client.sendmail("sepehr.tah@gmail.com", "sept@uturnmail.com","loltext")

sys.exit(0)

