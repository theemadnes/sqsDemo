# simple script to create messages in an SQS queue 
import boto.sqs
from boto.sqs.message import Message
import string
import random
import time 

conn_sqs = boto.sqs.connect_to_region("us-west-2")

my_queue = conn_sqs.get_queue('demoQueue1')

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

m = Message()
m.set_body(string_generator())
my_queue.write(m)
print "Added the following string to the queue: " + m
