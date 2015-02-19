# simple script to retrieve messages in an SQS queue and send an email via SNS to subscribers 
import time
import boto.sqs
from boto.sqs.message import Message

conn_sqs = boto.sqs.connect_to_region("us-west-2")

my_queue = conn_sqs.get_queue('demoQueue1')

if (my_queue.count() > 0):
	item = my_queue.get_messages(num_messages=1)
	print item[0].get_body()
	my_queue.delete_message(item[0])

else:
	print "No items in queue."


