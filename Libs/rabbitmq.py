# -*- coding: utf-8 -*-

import pika, os, logging
import re
import constant

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

        # self.connection.close()

    # Modify pg_rows value
    def modify_array_pg(self, pg_columns, pg_rows, ms_table, service, layerid, action):
        print 'Modify array'
        arr_modify = []
        indexOfObjectID = pg_columns.index("objectid")
        for arr in pg_rows:
            tmp = {
                # 'index': ms_table.lower(),
                'index': 'tbl_magma',
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

        print newStrArr
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

    # rb.create_json(insertStr)
    # rb.delete_json(deleteStr)
    # rb.update_json(updateStr)

    testArr = '''[{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":1,"thong":"3","tenphuche":" H/xd5/xb6 /xca/xb3  tn: Cu<i, t|ng, s0i, c|t, bft, s|t (25m tr| lrn).","lop":"4","chubien":"","tuoidc":"aQ/xd5/xb6 /xca/xb3 <in","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_1"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":2,"thong":"3","tenphuche":" H4 _  tC: Cu_i, t|ng, s0i, c|t, bft, s|t (25m tr| lrn).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_2"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":3,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_3"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":4,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, s t b n (th,m th p, b i b i v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_4"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":5,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, s t b n (th,m th p, b i b i v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_5"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":17,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, stt btn (th m th p, b i bii v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_17"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":6,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, s t b n (th,m th p, b i b i v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_6"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":7,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_7"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":8,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_8"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":9,"thong":"3","tenphuche":" H4 _  tC: Cu_i, thng, sti, ctt, b:t, s t (25m trs l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_9"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":42,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, stn, c t ia kho,ng, s t b n (thtm th p, b i b i v. trim tqch hi)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_42"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":10,"thong":"3","tenphuche":" H4 _  tC: Cu_i, thng, sti, ctt, b:t, s t (25m trs l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_10"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":11,"thong":"3","tenphuche":"Hp 8_ T_: Cuui, ttng, ssi, cct ,bbt, sst (25 met trl l)n)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_11"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":12,"thong":"3","tenphuche":" H4 _  tC: Cu_i, tnng, sii, ctt, btt, stt (25m trt l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_12"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":13,"thong":"3","tenphuche":"Hp 8_ T_: Cuui, ttng, ssi, cct ,bbt, sst (25 met trl l)n)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_13"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":14,"thong":"3","tenphuche":" H4 _  tC: Cu_i, tnng, sii, ctt, btt, stt (25m trt l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_14"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":15,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_15"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":16,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_16"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":46,"thong":"3","tenphuche":" H4 _  tC: Cu_i, tnng, s i, cht, b,t, s t (25m tr  l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_46"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":18,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_18"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":19,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, stt btn (th m th p, b i bii v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_19"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":20,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_20"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":21,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, stt btn (th m th p, b i bii v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_21"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":22,"thong":"3","tenphuche":" H4 _  tC: Cu_i, tnng, s i, cht, b,t, s t (25m tr  l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_22"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":23,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_23"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":24,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_24"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":25,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, stt btn (th m th p, b i bii v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_25"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":26,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_26"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":27,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_27"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":28,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, stt btn (th m th p, b i bii v. tr|m tdch hd)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_28"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":29,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_29"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":43,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, stn, c t ia kho,ng, s t b n (thtm th p, b i b i v. trim tqch hi)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_43"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":30,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, stt btn (th m thkp, b i bii v. tr|m tqch hi)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_30"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":31,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_31"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":32,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_32"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":33,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_33"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":34,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, s:n, c t  a khodng, stt bhn (thtm thsp, b,i bti vt trim tqch hi)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_34"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":44,"thong":"3","tenphuche":" H4 _  tC: Cu_i, tnng, s i, cht, b,t, s t (25m tr  l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_44"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":35,"thong":"3","tenphuche":" H4 _  tC: Cu_i, tnng, s i, cht, b,t, s t (25m tr  lsn).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_35"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":36,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_36"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":37,"thong":"3","tenphuche":"H","lop":"4","chubien":"","tuoidc":"T","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_37"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":38,"thong":"3","tenphuche":"Hp 8_ t_: Cuui, sPn, c t ia kho,ng, s t b n (th,m th p, b i b i v. trim tqch hi)","lop":"4","chubien":"","tuoidc":"apQ8_","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_38"},{"index":"tbl_magma","data":{"thanhphanth":"5","nhomtobd":"6","objectid":39,"thong":"3","tenphuche":" H4 _  tC: Cu_i, tnng, s i, cht, b,t, s t (25m tr  l n).","lop":"4","chubien":"","tuoidc":"aQ4 _ 4_C","khlt":"","tento":"7","gioi":"1","he":"2"},"id":"Tbl_fc_magma_sde_dia_tang_gdb_2_39"}]'''
    rb.delete_json(testArr)
