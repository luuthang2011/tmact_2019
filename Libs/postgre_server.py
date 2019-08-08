import psycopg2
import constant


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
        # query = """SELECT * FROM sde.f_48_66_a_tt_dt_region"""
        self.execute(query)
        rows = self.cursor.fetchall()
        print rows
        for row in rows:
            print "   ", row

    def select_schema(self, table):
        query = """SELECT column_name from information_schema.columns where table_name='%s'""" % table
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        print rows
        return rows


# Test Insert
if __name__ == '__main__':
    db = PostgresServer(r'ks')
    table = 'f_48_66_a_tt_dt_region'
    db.select_schema(table)
