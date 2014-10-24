# simple script to retrieve messages in an SQS queue and send an email via SNS to subscribers 
import time
import boto.sqs
import boto.sns
from boto.sqs.message import Message

conn_sqs = boto.sqs.connect_to_region("us-west-2")
conn_sns = boto.sns.connect_to_region("us-west-2")

my_queue = conn_sqs.get_queue('demoQueue1')

if (my_queue.count() > 0):
	item = my_queue.get_messages(num_messages=1)
	print item[0].get_body()
	conn_sns.publish(message=item[0].get_body(), subject='workerDemoEmail', topic='arn:aws:sns:us-west-2:789320537004:demoTopic1')
	my_queue.delete_message(item[0])

else:
	print "No items in queue."


