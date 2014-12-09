
import email, boto.sqs

# Read from STDIN into array of lines.
email_input = sys.stdin.readlines()

# email.FeedParser.feed() expects to receive lines one at a time
# msg holds the complete email Message object
parser = email.FeedParser.FeedParser()
msg = None
for msg_line in email_input:
   parser.feed(msg_line)
msg = parser.close()

from pprint import pprint
logFile=open('/mnt/spool/uturnmail/script_logs/uno.txt', 'w')
pprint (vars(msg),logFile)

#Will implement save email to a file first to examine it

#AMAZON SQS
#conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ465WWFWWSIUEKIQ', aws_secret_access_key='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')

#Get the queue
#queue = conn.get_queue('myqueue')