# -*- coding: utf-8 -*-

import pika, os, logging
logging.basicConfig()

from datetime import datetime
import time

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@52.220.224.131:5672/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='CREATE_JSON', durable=True, arguments={
                              'x-dead-letter-exchange': 'CREATE_JSONdead'
                      })

dt = datetime.strptime('2019-12-04 13:56:47.0590000', '%Y-%m-%d %H:%M:%S.%f0')
# dt = time.mktime(dt.timetuple()) * 1e3 + dt.microsecond / 1e3
a = '2019-12-04 13:56:47.0590000'.split(" ")
print '%s%s%s' % (a[0], 'T', a[1][:8])

#
# strs = '''[{"index": "Tbl_FC_DutGay",
#             "data": {
#               "ID_DA": 1,
#               "UpdatedBy": "PhuongHX",
#               "ObjectID": 103,
#               "LayerID": 0,
#               "LoaiDutgay": "Đứt gãy dự đoán",
#               "Phuongkeodai": "347.01419864",
#               "ID": 683,
#               "UpdatedDate": "2019-12-04 13:56:47.0590000",
#               "ID_DutGay": "Bđ.132_103",
#               "KHLT": "Đô.168",
#               "CreatedBy": "PhuongHX",
#               "CreatedDate": "2019-12-04 13:56:47.0590000",
#               "LayerName": "DutGay",
#               "IsDeAn": false
#             },
#             "id": 683
#           }]'''
# strs = strs.decode('utf8')
#
# channel.basic_publish(exchange='',
#                       routing_key='CREATE_JSON',
#                       body='''[{"index": "Tbl_FC_DutGay",
#                                 "data": {
#                                   "ID_DA": 1,
#                                   "UpdatedBy": "PhuongHX",
#                                   "ObjectID": 103,
#                                   "LayerID": 0,
#                                   "LoaiDutgay": "Đứt gãy dự đoán",
#                                   "ID": 688,
#                                   "UpdatedDate": "1575450099000",
#                                   "ID_DutGay": "Bđ.132_103",
#                                   "KHLT": "Đô.168",
#                                   "CreatedBy": "PhuongHX",
#                                   "CreatedDate": "1575450099000",
#                                   "LayerName": "DutGay",
#                                   "IsDeAn": false
#                                 },
#                                 "id": 688
#                               }]''')
# print(" [x] Sent 'Hello World!'")

connection.close()