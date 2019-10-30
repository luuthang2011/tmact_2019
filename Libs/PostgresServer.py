import psycopg2
import constant
import itertools
import datetime

fs = '%Y-%m-%d %H:%M:%S.%f0'


class DB:
    def __init__(self, in_data):
        print 'Start PostgreSQL'
        global input_data
        input_data = in_data
        # # self.database = constant.DATABASE_POSTGRES
        # self.connection = psycopg2.connect(
        #     database=constant.DATABASE_POSTGRES,
        #     user=constant.USER_POSTGRES,
        #     password=constant.PASSWORD_POSTGRES,
        #     host=constant.HOST_POSTGRES,
        #     port=constant.PORT_POSTGRES)
        # self.cursor = self.connection.cursor()
        # print 'Connected success!'

    # def execute(self, query):
    #     results = self.cursor.execute(query)
    #     # print results

    def init_connect(self):
        # self.database = constant.DATABASE_POSTGRES
        self.connection = psycopg2.connect(
            database=constant.DATABASE_POSTGRES,
            user=constant.USER_POSTGRES,
            password=constant.PASSWORD_POSTGRES,
            host=constant.HOST_POSTGRES,
            port=constant.PORT_POSTGRES)
        self.cursor = self.connection.cursor()
        print 'Connected PostgreSQL success!'


    def select(self, query):
        # q = """SELECT * FROM sde.f_48_66_a_tt_dt_region"""
        # self.cursor.execute(q)
        self.init_connect()
        print 'Query: %s' % query
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        self.cursor.close()
        self.connection.close()

        # print rows
        # for row in rows:
        #     print "   ", row
        return rows

    def select_schema(self, table):
        self.init_connect()
        print 'SELECT table schema'
        query = r"""SELECT column_name from information_schema.columns where table_name='%s'""" % table
        # query = r"""SELECT column_name from information_schema.columns where table_name='%s'""" % input_data
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Convert tuple to array
        lists = list(itertools.chain.from_iterable(rows))

        # Get subset or list
        # subset_of_list = {'shape', 'id'}
        subset_of_list = {'shape', 'id', 'id_da'}
        result = [l for l in lists if l not in subset_of_list]

        self.cursor.close()
        self.connection.close()

        return result

    def query_builder(self, columns, table):
        columns_strip = str(columns).strip('[]')
        columns_replace = columns_strip.replace("'", "").replace('"', '')
        # query = r'''SELECT %s FROM sde.%s LIMIT 2''' % (columns_replace, table)
        # query = r'''SELECT %s , 11111 AS IsDeAn FROM sde.%s LIMIT 2''' % (columns_replace, table)
        query = r'''SELECT %s FROM sde.%s''' % (columns_replace, table)

        return query

    def query_builder_with_custom_field(self, id_dean, columns, table):
        print "Ma De an MS %s" % id_dean
        columns_strip = str(columns).strip('[]')
        columns_replace = columns_strip.replace("'", "").replace('"', '')
        now = datetime.datetime.now()
        now_fs = now.strftime(fs)

        # query = r'''SELECT %s, '%s' AS ID_DA, '%s' AS CreatedDate, '%s' AS UpdatedDate , 1 AS IsDeAn FROM sde.%s''' % (columns_replace, id_dean, now_fs, now_fs, table)

        query = r'''SELECT %s, '%s' AS ID_DA, '%s' AS CreatedDate, '%s' AS UpdatedDate FROM sde.%s''' % (
        columns_replace, id_dean, now_fs, now_fs, table)

        print 'Custom query: %s' % query

        self.query_get_id_dean(table)
        return query

    def query_get_id_dean(self, table):
        query = r'''SELECT "id_da" FROM sde.%s LIMIT 1''' % ( table )
        print 'Query select: %s' % query
        self.init_connect()
        row = self.select(query)
        self.cursor.close()
        self.connection.close()
        if len(row):
            id_da = row[0][0]
            print 'ID De An PG: %s' % id_da
            return id_da
        else:
            print 'row: %s' % row
            return 0



    # Replace None Value to empty string
    def replace_none_value(self, tuples):
        return tuple(
            (item if item else '') for item in tuples
        )

    def validate_data(self, rows):
        print 'Validate null value'
        results = []
        for row in rows:
            results.append(self.replace_none_value(row))

        return results


# Test Insert
if __name__ == '__main__':
    db = DB(r'ks')
    # table = 'fc_magma'
    # table = 'f_48_94_c_chu_dt_region'
    # table = 'phuonghx_magma1'
    table = 'magmaadcsawsfaw'
    columns = db.select_schema(table)
    tmp = columns[:]
    # print columns
    tmp.append('isDean')
    print tmp
    # columns_strip = str(columns).strip('[]')
    # columns_replace = columns_strip.replace("'", "").replace('"', '')
    # query = r'''SELECT %s FROM sde.%s LIMIT 10''' % (columns_replace, table)
    # query = r'''SELECT objectid, id, tenphuche, tuoidc, gioi, he, thong, lop, thanhphanth, nhomtobd FROM sde.%s LIMIT 10''' % table

    # query = db.query_builder(columns, table)
    query = db.query_builder_with_custom_field(1, columns, table)
    # print query
    # results = db.select(query)
    # print results
    # new_results = []
    # for row in results:
    #     print row
        # new_results.append(db.replace_none_value(row))

    # print new_results
