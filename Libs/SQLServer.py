# -*- coding: utf-8 -*-

import pyodbc
import constant


class DB:
    def __init__(self, database):
        print 'Start connect SQL Server'
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
        print 'Connected success!'

    def execute(self, query):
        self.cursor.execute(query)

    def insert(self, table, columns, values):
        f = ', '.join(map(str, columns))
        v = str(values).strip('[]')

        insert_script = r'''INSERT INTO %s ( %s ) VALUES ( %s )''' % (table, f, v)
        # print insert_script
        self.execute(insert_script)
        self.connection.commit()

    def multiple_insert(self, table, fields, values):
        f = ', '.join(map(str, fields))
        v = str(values).strip('[]')

        insert_script = r'''INSERT INTO %s ( %s ) VALUES %s ''' % (table, f, v)
        # print insert_script
        self.execute(insert_script)
        self.connection.commit()

    def update_value_null(self, table, field, value):
        print 'Update layerName and layerID'
        script = '''UPDATE %s SET %s = '%s' WHERE %s IS NULL''' % (table, field, value, field)
        print script
        self.execute(script)
        self.connection.commit()

    def delete_row_service(self, table, column, service):
        print 'Start delete Service'
        script = '''DELETE FROM %s WHERE %s='%s' ''' % (table, column, service)
        print script
        self.cursor.execute(script)
        self.connection.commit()

# Test Insert
if __name__ == '__main__':
    db = DB(r'CSDLTayBac')
    # query = 'SELECT * FROM CSDLTayBac.dbo.Tbl_DVTC'
    # db.execute(query)
    # db.execute(INSERT_SCRIPT)
    table = 'CSDLTayBac.dbo.Tbl_FC_Magma'
    columns = ["ObjectID", "TenPhucHe", "TuoiDC", "Gioi", "He", "Thong",
               "Lop", "ThanhPhanTH", "NhomToBD", "TenTo", "ID_DanhPhap",
               "ID_TyLe", "KHLT", "ChuBien", "NamNopLT"]

    values = [2, 'TenPhucHe', 'TuoiDC', 'Gioi', 'He', 'Thong',
              'Lop', 'ThanhPhanTH', 'NhomToBD', 'TenTo', 'ID_DanhPhap',
              'ID_TyLe', 'KHLT', 'ChuBien', 'NamNopLT']
    # db.insert(table, columns, values)

    column = 'LayerName'
    service = 'aaaaa'

    db.delete_row_service(table, column,  service)

