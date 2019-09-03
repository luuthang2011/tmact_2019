# -*- coding: utf-8 -*-

import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@34.87.22.131:5672/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='CREATE_JSON', durable=True, arguments={
                              'x-dead-letter-exchange': 'CREATE_JSONdead'
                      })

channel.basic_publish(exchange='',
                      routing_key='CREATE_JSON',
                      body='''[{
                            "index": "tbl_dean",
                            "id": "2",
                            "data": {
                                "ID": "2",
                                "chuBien": "ThangLQ"
                            }
                        },{
                            "index": "tbl_dean",
                            "id": "3",
                            "data": {
                                "ID": "3",
                                "chuBien": "ThangLQ"
                            }
                        }]''')
print(" [x] Sent 'Hello World!'")

connection.close()