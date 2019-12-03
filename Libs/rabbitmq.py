# -*- coding: utf-8 -*-

import pika, os, logging
# import re
import constant
import json

logging.basicConfig()


class Rabbit:
    def __init__(self):
        print 'Start init Rabbit connection'
        # Parse CLODUAMQP_URL (fallback to localhost)
        self.url = os.environ.get('CLOUDAMQP_URL', constant.Rabbit)
        self.params = pika.URLParameters(self.url)
        self.params.socket_timeout = 30

    def init_connect(self):
        self.connection = pika.BlockingConnection(self.params)  # Connect to CloudAMQP
        self.channel = self.connection.channel()  # start a channel

    def create_json(self, str):
        print 'Start Create json'
        print str
        print '-------------------------'

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
    def modify_array_pg(self, pg_columns, pg_rows, ms_table, service, layerid, user, action):
        print 'Modify array'
        arr_modify = []
        arr_str = '['
        indexOfObjectID = pg_columns.index("objectid")
        print 'Start build str for Rabbit'
        for arr in pg_rows:
            id_index = pg_columns.index('id')
            # id_insert = service + '_' + str(layerid) + '_' + str(arr[indexOfObjectID])
            id_insert = arr[id_index]
            tmp = {
                # 'index': ms_table.lower(),
                'index': ms_table,
                # 'index': 'tbl_magma',
                   'id': id_insert}
            # Add tuple data if action equal CREATE
            if action == 'CREATE':
                tupleObject = {}
                for column in pg_columns:
                    # @Todo: Need change lower case key in Rabbit
                    if column not in ['rbg_color', 'red', 'green', 'blue']:
                        OBJ_UPPERCASE = constant.OBJ_CASE
                        column_match_case = column
                        if column in OBJ_UPPERCASE:
                            column_match_case = OBJ_UPPERCASE[column]

                        indexTuple = pg_columns.index(column)
                        # tupleObject[column] = arr[indexTuple]
                        value_index = arr[indexTuple]
                        if isinstance(value_index, str):
                            value_index = value_index.replace("'", '')
                            value_index = value_index.replace('"', '')
                        # tupleObject[column_match_case] = arr[indexTuple]
                        tupleObject[column_match_case] = value_index

                # CreatedBy and UpdatedBy
                tupleObject['CreatedBy'] = user
                tupleObject['UpdatedBy'] = user
                tupleObject['ID'] = id_insert
                tmp['data'] = tupleObject
                print 'Rabbit string: '
                print tmp
                arr_str += json.dumps(tmp).decode('utf-8') + ","
            arr_modify.append(tmp)
        if action == 'CREATE':
            arr_str = arr_str[:-1]
            arr_str += "]"
            # print "arr_str: ", arr_str
            return arr_str
        # Array to string
        strArr = """%s""" % arr_modify
        # Replace single quote to double quote
        # newStrArr = strArr.replace("'", '"').replace('\\', "/")
        newStrArr = strArr.replace("'", '"')

        # print newStrArr
        #
        # if action == "CREATE":
        #     self.create_json('''%s''' % newStrArr)
        # elif action == "DELETE":
        #     self.delete_json('''%s''' % newStrArr)

        return newStrArr

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
