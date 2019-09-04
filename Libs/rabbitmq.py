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

        # self.connection.close()

    def update_json(self, str):
        print 'Start Update json'
        self.channel.queue_declare(queue='UPDATE_JSON', durable=True, arguments={
            'x-dead-letter-exchange': 'UPDATE_JSONdead'
        })

        self.channel.basic_publish(exchange='',
                                   routing_key='UPDATE_JSON',
                                   body=str)
        print(" [x] Updated!'")

        # self.connection.close()

    def delete_json(self, str):
        print 'Start Delete json'
        self.channel.queue_declare(queue='DELETE_JSON', durable=True, arguments={
            'x-dead-letter-exchange': 'DELETE_JSONdead'
        })

        self.channel.basic_publish(exchange='',
                                   routing_key='DELETE_JSON',
                                   body=str)
        print(" [x] Deleted!'")

        # self.connection.close()

    def modify_array_pg(self, pg_columns, arrs, ms_table, service, layerid):
        print 'Modify array'
        arr_modify = []
        indexOfObjectID = pg_columns.index("objectid")
        # @Todo: modify array
        print pg_columns
        for arr in arrs:
            tmp = {
                # 'index': ms_table.lower(),
                'index': 'tbl_magma',
                   'id': service + '_' + str(layerid) + '_' + str(arr[indexOfObjectID])}
            tupeObject = {}
            for column in pg_columns:
                if column not in ['objectid', 'tuoidc', 'gioi', 'he', 'thong', 'lop', 'thanhphanth', 'nhomtobd', 'tento', 'id_danhphap', 'id_tyle', 'khlt', 'chubien', 'namnoplt']:
                    indexTupe = pg_columns.index(column)
                    tupeObject[column] = arr[indexTupe]

            tmp['data'] = tupeObject
            arr_modify.append(tmp)
        # print arr_modify
        strArr = """%s""" % arr_modify
        # print strArr


        ars = '''[
                {"index": "tbl_magma",
                    "id": "fc_magma_1_10"
                    "data": {
                        "tenPhucHe": "dasd"
                    }
                },
                {"index": "tbl_magma",
                    "id": "fc_magma_1_11"
                    "data": {
                        "tenPhucHe": "Hsadsa"
                    }
                }
                ]'''

        # self.create_json(strArr)
        self.create_json(ars)

        return arr_modify

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':
    print 'Unit test main rabbit'
    rb = Rabbit()

    insertStr = '''[{
                        "index": "tbl_dean",
                        "id": "service_layerid_11",
                        "data": {
                           "chuBien": "ThangLQ",
                            "tacgia": "PhuongHX"
                        }
                    },{
                        "index": "tbl_dean",
                        "id": "service_layerid_12",
                        "data": {
                            "chuBien": "ThangLQ",
                            "tacgia": "PhuongHX"
                        }
                    }]'''

    updateStr = '''[{
                        "index": "tbl_dean",
                        "id": "11",
                        "data": {
                            "chuBien": "PhuongHX"
                        }
                    },{
                        "index": "tbl_dean",
                        "id": "12",
                        "data": {
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


