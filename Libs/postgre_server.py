import psycopg2
import constant
import itertools


# con = psycopg2.connect(
#     database=constant.DATABASE_POSTGRES,
#     user=constant.USER_POSTGRES,
#     password=constant.PASSWORD_POSTGRES,
#     host=constant.HOST_POSTGRES,
#     port=constant.PORT_POSTGRES)
#
# cursor = con.cursor()
#
# print("Database opened successfully")


class PostgresServer:
    def __init__(self, database):
        self.database = database
        self.connection = psycopg2.connect(
            database=constant.DATABASE_POSTGRES,
            user=constant.USER_POSTGRES,
            password=constant.PASSWORD_POSTGRES,
            host=constant.HOST_POSTGRES,
            port=constant.PORT_POSTGRES)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        results = self.cursor.execute(query)
        # print results

    def select(self, query):
        # q = """SELECT * FROM sde.f_48_66_a_tt_dt_region"""
        # q = """SELECT * FROM sde.f_48_66_a_tt_dt_region"""
        # self.cursor.execute(q)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        print rows
        # for row in rows:
        #     print "   ", row

    def select_schema(self, table):
        query = """SELECT column_name from information_schema.columns where table_name='%s'""" % table
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Convert tuple to array
        lists = list(itertools.chain.from_iterable(rows))

        # Get subset or list
        subset_of_list = {'shape', 'id'}
        result = [l for l in lists if l not in subset_of_list]
        print lists
        print result
        return result

    def query_builder(self, columns):
        columns_strip = str(columns).strip('[]')
        columns_replace = columns_strip.replace("'", "").replace('"', '')
        # query = r'''SELECT %s FROM sde.%s LIMIT 10''' % (columns_replace, table)
        query = r'''SELECT %s FROM sde.%s''' % (columns_replace, table)

        return query


# Test Insert
if __name__ == '__main__':
    db = PostgresServer(r'ks')
    # table = 'f_48_66_a_tt_dt_region'
    table = 'fc_magma'
    columns = db.select_schema(table)
    # print columns
    # columns_strip = str(columns).strip('[]')
    # columns_replace = columns_strip.replace("'", "").replace('"', '')
    # query = r'''SELECT %s FROM sde.%s LIMIT 10''' % (columns_replace, table)
    # query = r'''SELECT objectid, id, tenphuche, tuoidc, gioi, he, thong, lop, thanhphanth, nhomtobd FROM sde.%s LIMIT 10''' % table

    query = db.query_builder(columns)
    print query
    db.select(query)
