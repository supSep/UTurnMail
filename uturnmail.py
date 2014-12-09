# Read from STDIN into array of lines.
email_input = sys.stdin.readlines()

# email.FeedParser.feed() expects to receive lines one at a time
# msg holds the complete email Message object
parser = email.FeedParser.FeedParser()
msg = None
for msg_line in email_input:
   parser.feed(msg_line)
msg = parser.close()