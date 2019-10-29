# -*- coding: utf-8 -*-

import pyodbc
import constant


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
        print 'Start insert'
        f = ', '.join(map(str, columns))
        v = str(values).strip('[]')

        insert_script = r'''INSERT INTO %s ( %s ) VALUES ( %s )''' % (table, f, v)
        # print insert_script
        self.init_connect()
        self.cursor.execute(insert_script)
        self.connection.commit()
        self.cursor.close()

    def multiple_insert(self, table, fields, values):
        print 'Start multiple_insert'
        f = ', '.join(map(str, fields))
        v = str(values).strip('[]')

        insert_script = r'''INSERT INTO %s ( %s ) VALUES %s ''' % (table, f, v)
        print 'multiple_insert script: %s' % insert_script
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

    def select_id_dean(self, value):
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
    db.select_id_dean('DOVEDIACHAT_LTD11')

