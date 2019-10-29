# -*- coding: utf-8 -*-

import pika, os, logging
import re
import constant

logging.basicConfig()


class Rabbit:
    def __init__(self):
        print 'Start init Rabbit connection'
        # Parse CLODUAMQP_URL (fallback to localhost)
        self.url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@52.220.224.131:5672/%2f')
        self.params = pika.URLParameters(self.url)
        self.params.socket_timeout = 30

    def init_connect(self):
        self.connection = pika.BlockingConnection(self.params)  # Connect to CloudAMQP
        self.channel = self.connection.channel()  # start a channel

    def create_json(self, str):
        print 'Start Create json'
        self.init_connect()

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
        self.init_connect()

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
        self.init_connect()

        self.channel.queue_declare(queue='DELETE_JSON', durable=True, arguments={
            'x-dead-letter-exchange': 'DELETE_JSONdead'
        })

        self.channel.basic_publish(exchange='',
                                   routing_key='DELETE_JSON',
                                   body=str)
        print(" [x] Deleted!'")

        self.connection.close()

    # Modify pg_rows value
    def modify_array_pg(self, pg_columns, pg_rows, ms_table, service, layerid, action):
        print 'Modify array'
        arr_modify = []
        indexOfObjectID = pg_columns.index("objectid")
        for arr in pg_rows:
            tmp = {
                # 'index': ms_table.lower(),
                'index': ms_table,
                # 'index': 'tbl_magma',
                   'id': service + '_' + str(layerid) + '_' + str(arr[indexOfObjectID])}
            # Add tuple data if action equal CREATE
            if action == 'CREATE':
                tupleObject = {}
                for column in pg_columns:
                    # @Todo: Need change lower case key in Rabbit
                    if column not in ['id_danhphap', 'id_tyle', 'namnoplt']:
                        indexTuple = pg_columns.index(column)
                        tupleObject[column] = arr[indexTuple]
                tmp['data'] = tupleObject

                # print tmp

            arr_modify.append(tmp)
        # Array to string
        strArr = """%s""" % arr_modify
        # Replace single quote to double quote
        newStrArr = strArr.replace("'", '"').replace('\\', "/")

        # print newStrArr
        #
        # if action == "CREATE":
        #     self.create_json('''%s''' % newStrArr)
        # elif action == "DELETE":
        #     self.delete_json('''%s''' % newStrArr)

        return newStrArr

    # def convert_case(self, case):
    #     for c in constant.MATCHING_CASE:
    #

    # def __del__(self):
    #     self.connection.close()

#
# if __name__ == '__main__':
#     print 'Unit test main rabbit'
#     rb = Rabbit()
#
#     insertStr = '''[{
#                         "index": "tbl_dean",
#                         "id": "service_layerid_11",
#                         "data": {
#                            "chuBien": "ThangLQ",
#                             "tacgia": "PhuongHX"
#                         }
#                     },{
#                         "index": "tbl_dean",
#                         "id": "service_layerid_12",
#                         "data": {
#                             "chuBien": "ThangLQ",
#                             "tacgia": "PhuongHX"
#                         }
#                     }]'''
#
#     updateStr = '''[{
#                         "index": "tbl_dean",
#                         "id": "11",
#                         "data": {
#                             "chuBien": "PhuongHX"
#                         }
#                     },{
#                         "index": "tbl_dean",
#                         "id": "12",
#                         "data": {
#                            "chuBien": "PhuongHX"
#                         }
#                     }]'''
#
#     deleteStr = '''[{
#                         "index": "tbl_dean",
#                         "id": "11"
#                     },{
#                         "index": "tbl_dean",
#                         "id": "12"
#                     },{
#                         "index": "tbl_dean",
#                         "id": "987654"
#                     }]'''
#
#     # rb.create_json(insertStr)
#     # rb.delete_json(deleteStr)
#     # rb.update_json(updateStr)
#
#     testArr = '''[{"index":"tbl_fc_magma","id":"Tbl_FC_Magma_sde_dia_tang_gdb_5_3"}]'''
#     rb.delete_json(testArr)
#     # rb.create_json(testArr)
