# -*- coding: utf-8 -*-

import pika, os, logging

logging.basicConfig()


class Rabbit:
    def __init__(self):
        print 'Start init Rabbit connection'

        # Parse CLODUAMQP_URL (fallback to localhost)
        self.url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@34.87.22.131:5672/%2f')
        self.params = pika.URLParameters(self.url)
        self.params.socket_timeout = 30

        self.connection = pika.BlockingConnection(self.params)  # Connect to CloudAMQP
        self.channel = self.connection.channel()  # start a channel

    def create_json(self, str):
        print 'Start Create json'
        self.channel.queue_declare(queue='CREATE_JSON', durable=True, arguments={
            'x-dead-letter-exchange': 'CREATE_JSONdead'
        })

        self.channel.basic_publish(exchange='',
                                   routing_key='CREATE_JSON',
                                   body=str)
        print(" [x] Created!'")

        self.connection.close()

    def update_json(self, str):
        print 'Start Update json'
        self.channel.queue_declare(queue='UPDATE_JSON', durable=True, arguments={
            'x-dead-letter-exchange': 'UPDATE_JSONdead'
        })

        self.channel.basic_publish(exchange='',
                                   routing_key='UPDATE_JSON',
                                   body=str)
        print(" [x] Updated!'")

        self.connection.close()

    def delete_json(self, str):
        print 'Start Delete json'
        self.channel.queue_declare(queue='DELETE_JSON', durable=True, arguments={
            'x-dead-letter-exchange': 'DELETE_JSONdead'
        })

        self.channel.basic_publish(exchange='',
                                   routing_key='DELETE_JSON',
                                   body=str)
        print(" [x] Deleted!'")

        self.connection.close()

    def modify_array(self, arrs, ms_table, service, layerid):
        print 'Modify array'
        arr_modify = []
        for arr in arrs:
            tmp = {}
            tmp.index = ms_table
            tmp.id = service + '_' + layerid + '_' + arr.objectID
            tmp.data = arr
            tmp.data.ID = service + '_' + layerid + '_' + arr.objectID
            arr_modify.append(tmp)

        return arr_modify


if __name__ == '__main__':
    print 'Unit test main rabbit'
    rb = Rabbit()

    insertStr = '''[{
                "index": "tbl_dean",
                "id": "11",
                "data": {
                    "ID": "11",
                    "chuBien": "ThangLQ"
                }
            },{
                "index": "tbl_dean",
                "id": "12",
                "data": {
                    "ID": "12",
                    "chuBien": "ThangLQ"
                }
            }]'''

    updateStr = '''[{
                    "index": "tbl_dean",
                    "id": "11",
                    "data": {
                        "ID": "11",
                        "chuBien": "PhuongHX"
                    }
                },{
                    "index": "tbl_dean",
                    "id": "12",
                    "data": {
                        "ID": "12",
                        "chuBien": "PhuongHX"
                    }
                }]'''

    deleteStr = '''[{
                        "index": "tbl_dean",
                        "id": "11"
                    },{
                        "index": "tbl_dean",
                        "id": "12"
                    },{
                        "index": "tbl_dean",
                        "id": "987654"
                    }]'''

    rb.create_json(insertStr)
    # rb.delete_json(deleteStr)
    # rb.update_json(updateStr)
