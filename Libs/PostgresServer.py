import psycopg2
import constant
import itertools


class DB:
    def __init__(self, in_data):
        print 'Start connect PostgreSQL'
        global input_data
        input_data = in_data
        # self.database = constant.DATABASE_POSTGRES
        self.connection = psycopg2.connect(
            database=constant.DATABASE_POSTGRES,
            user=constant.USER_POSTGRES,
            password=constant.PASSWORD_POSTGRES,
            host=constant.HOST_POSTGRES,
            port=constant.PORT_POSTGRES)
        self.cursor = self.connection.cursor()
        print 'Connected success!'

    def execute(self, query):
        results = self.cursor.execute(query)
        # print results

    def select(self, query):
        # q = """SELECT * FROM sde.f_48_66_a_tt_dt_region"""
        # self.cursor.execute(q)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        # print rows
        # for row in rows:
        #     print "   ", row
        return rows

    def select_schema(self, table):
        print 'SELECT table schema'
        query = r"""SELECT column_name from information_schema.columns where table_name='%s'""" % table
        # query = r"""SELECT column_name from information_schema.columns where table_name='%s'""" % input_data
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Convert tuple to array
        lists = list(itertools.chain.from_iterable(rows))

        # Get subset or list
        subset_of_list = {'shape', 'id'}
        result = [l for l in lists if l not in subset_of_list]

        return result

    def query_builder(self, columns, table):
        columns_strip = str(columns).strip('[]')
        columns_replace = columns_strip.replace("'", "").replace('"', '')
        # query = r'''SELECT %s FROM sde.%s LIMIT 2''' % (columns_replace, table)
        query = r'''SELECT %s FROM sde.%s''' % (columns_replace, table)

        return query

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
    # table = 'f_48_66_a_tt_dt_region'
    # table = 'fc_magma'
    table = 'f_48_94_c_chu_dt_region'
    columns = db.select_schema(table)
    print columns
    # columns_strip = str(columns).strip('[]')
    # columns_replace = columns_strip.replace("'", "").replace('"', '')
    # query = r'''SELECT %s FROM sde.%s LIMIT 10''' % (columns_replace, table)
    # query = r'''SELECT objectid, id, tenphuche, tuoidc, gioi, he, thong, lop, thanhphanth, nhomtobd FROM sde.%s LIMIT 10''' % table

    query = db.query_builder(columns, table)
    # print query
    results = db.select(query)
    # print results
    new_results = []
    for row in results:
        new_results.append(db.replace_none_value(row))

    print new_results
