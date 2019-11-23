# -*- coding: utf-8 -*-

import pyodbc
# import psycopg2.extensions
# psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
# psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import json
import codecs
import constant
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# import sys
#
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
#
# sys.stdin = codecs.getreader('utf_8')(sys.stdin)


def check(f):
    if isinstance(f, str):
        return str(f)
    else:
        return f


def make_unicode_str(values):
    string = "("
    for v in values:
        if isinstance(v, str):
            string = string + " N'" + str(v) + "', "
        else:
            string += str(v) + ", "
    string = string[:-2]
    string += ")"
    # print string
    return string


class DB:
    def __init__(self, database):
        print 'Start connect SQL Server'

    def init_connect(self):
        self.database = constant.DATABASE_SQL
        self.connection = \
            pyodbc.connect(r'''Driver=%s;
                                       Server=%s;
                                       DATABASE=%s;
                                       UID=%s;
                                       PWD=%s;
                                       ''' % (constant.DRIVER_SQL, constant.SERVER_SQL,
                                              self.database, constant.USER_SQL, constant.PASSWORD_SQL))
        self.cursor = self.connection.cursor()
        print 'Connected SQL success!'

    def execute(self, query):
        self.cursor.execute(query)

    def insert(self, table, columns, values):
        print 'Start insert to SQL Server'
        f = ', '.join(map(str, columns))
        v = str(values).strip('[]')

        insert_script = r'''INSERT INTO %s ( %s ) VALUES ( %s )''' % (table, f, v)
        # print insert_script
        self.init_connect()
        self.cursor.execute(insert_script)
        self.connection.commit()
        self.cursor.close()

    def multiple_insert(self, table, fields, values):
        print 'Start multiple_insert to SQL Server:'
        print type(values)
        f = ', '.join(map(str, fields))
        v = str(values).strip('[]')

        insert_str = ''
        for vv in values:
            # # one_row = json.dumps(vv).decode('utf-8')
            # one_row = str(vv)
            # # encoded = [check(t) for t in vv]
            # one_row = one_row.replace('"', "'").replace('[', '(').replace(']', ')').replace(", '", ", N'")

            print '------------------------------'
            encoded = make_unicode_str(vv)
            print encoded
            insert_str += encoded
            insert_str += ','
        insert_str = insert_str[:-1]

        insert_script = '''INSERT INTO %s ( %s ) VALUES %s ''' % (table, f, insert_str)
        insert_script = insert_script.decode('utf8', "ignore")
        print '***********************************'
        print insert_script

        self.init_connect()
        self.cursor.execute(insert_script)
        self.connection.commit()
        self.cursor.close()

    def update_value_null(self, table, field, value):
        print 'Update layerName and layerID'
        script = '''UPDATE %s SET %s = '%s' WHERE %s IS NULL''' % (table, field, value, field)
        print script
        self.init_connect()
        self.cursor.execute(script)
        self.connection.commit()
        self.cursor.close()

    def select(self, table, columns, service, layerid):
        print 'Start select ID Dean'

        columns = ', '.join(str(x) for x in columns)
        script = '''SELECT %s FROM %s WHERE layername='%s' AND layerid='%s' ''' % (columns, table, service, layerid)
        print script
        self.init_connect()
        self.cursor.execute(script)
        rows = self.cursor.fetchall()
        self.cursor.close()
        print rows
        return rows

    def select_id_dean(self, value):
        print 'Start select ID Dean'
        script = '''SELECT TOP 1 id FROM %s WHERE %s = '%s' ''' % ("Tbl_QLDA", "MaDeAn", value)
        print script
        self.init_connect()
        self.cursor.execute(script)
        row = self.cursor.fetchone()
        self.cursor.close()
        if None == row:
            print 'Row is None'
            return 0
        else:
            print 'ID De An MS: %s' % row
            return row[0]

    def select_id_luutru(self, value):
        print 'Start select ID Bao Cao Luu Tru'
        script = '''SELECT TOP 1 id FROM %s WHERE %s = '%s' ''' % ("Tbl_BaoCaoDiaChat", "KHLT", value)
        print script
        self.init_connect()
        self.cursor.execute(script)
        row = self.cursor.fetchone()
        self.cursor.close()
        if None == row:
            print 'Row is None'
            return 0
        else:
            print 'ID Bao Cao Luu Tru MS: %s' % row
            return row[0]

    def delete_row_service(self, table, column, service):
        print 'Start delete Service'
        script = '''DELETE FROM %s WHERE %s='%s' ''' % (table, column, service)
        print script
        self.init_connect()
        self.cursor.execute(script)
        self.connection.commit()
        self.cursor.close()


# Test Insert
if __name__ == '__main__':
    db = DB(r'CSDLTayBacUAT')

    db.init_connect()
    # query = 'SELECT * FROM CSDLTayBacUAT.dbo.Tbl_QLDA'
    # db.execute(INSERT_SCRIPT)

    # table = 'CSDLTayBac.dbo.Tbl_FC_Magma'
    # table = 'Tbl_QLDA'

    # columns = ["ObjectID", "TenPhucHe", "TuoiDC", "Gioi", "He", "Thong",
    #            "Lop", "ThanhPhanTH", "NhomToBD", "TenTo", "ID_DanhPhap",
    #            "ID_TyLe", "KHLT", "ChuBien", "NamNopLT"]
    #
    # values = [2, 'TenPhucHe', 'TuoiDC', 'Gioi', 'He', 'Thong',
    #           'Lop', 'ThanhPhanTH', 'NhomToBD', 'TenTo', 'ID_DanhPhap',
    #           'ID_TyLe', 'KHLT', 'ChuBien', 'NamNopLT']
    # # db.insert(table, columns, values)
    #
    # column = 'LayerName'
    # service = 'aaaaa'
    #
    # db.delete_row_service(table, column,  service)
    # db.select_id_dean('DOVEDIACHAT_LTD11')

    # query = "INSERT INTO Tbl_FC_TramTich ( objectid, tenhetang, phuhetang, tuoidc, gioi, he, thong, thanhphanth, nhomtobd, tento, danhphap_bd, tyle_bd, hoathach, khlt, chubien, namnoplt, tap_phan, isdean, id_tramtich, ID_DA, CreatedDate, UpdatedDate, CreatedBy, UpdatedBy, LayerName, LayerID ) VALUES (127, N'H\xe1\xbb\x87 t\xe1\xba\xa7ng M\xc6\xb0\xe1\xbb\x9dng Hinh ', N'Ph\xe1\xbb\xa5 h\xe1\xbb\x87 t\xe1\xba\xa7ng d\xc6\xb0\xe1\xbb\x9bi', N'J\xc3\x87\xc3\x82\xc2\xa3', N'Mesozoi', N'Jura', N'Kh\xc3\xb4ng x\xc3\xa1c \xc4\x91\xe1\xbb\x8bnh', N'Tr\xe1\xba\xa7m t\xc3\xadch phun tr\xc3\xa0o v\xc3\xa0 phun tr\xc3\xa0o th\xe1\xbb\xb1c s\xe1\xbb\xb1: Riolit pocfia, fenzitofia xen th\xe1\xba\xa5u k\xc3\xadnh b\xe1\xbb\x99t k\xe1\xba\xbft tufogen c\xc3\xa1t k\xe1\xba\xbft tufogen. Ph\xe1\xba\xa7n \xc4\x91\xc3\xa1y c\xc3\xb3 cu\xe1\xbb\x99i k\xe1\xba\xbft', N'V\xc3\xb9ng T\xc3\xa2y Nam Th\xc6\xb0\xe1\xbb\x9dng Xu\xc3\xa2n', N'T\xe1\xbb\x9d \xc4\x90\xe1\xbb\x93ng Tr\xe1\xba\xa7u', N'E-48-7-D', N'1:50.000', N'Kh\xc3\xb4ng c\xc3\xb3 th\xc3\xb4ng tin', N'B\xc4\x91.153', N'Phan V\xc4\x83n \xc3\x81i', N'1993', N'Kh\xc3\xb4ng c\xc3\xb3 th\xc3\xb4ng tin', N'1', N'B\xc4\x91.153_127', N'1194', N'2019-11-17 14:22:12.2000000', N'2019-11-17 14:22:12.2000000', N'PhuongHX', N'PhuongHX', N'TramTich', N'0')"
    #
    # query = query.decode('utf8', "ignore")
    # print query
    #
    # db.init_connect()
    # db.cursor.execute(query)
    # db.cursor.execute(query)
    # db.connection.commit()
    # db.cursor.close()

    db.select('Tbl_FC_TramTich', 'objectid, tenhetang, phuhetang, tuoidc','TramTich',0)