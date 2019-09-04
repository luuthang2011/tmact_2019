import SQLServer
import PostgresServer
import rabbitmq


class FlowProcess:
    def __init__(self):
        print 'Init Flow Process...'
        global pgServer, msServer, Rabbit
        pgServer = PostgresServer.DB('')
        msServer = SQLServer.DB('')
        Rabbit = rabbitmq.Rabbit()

    def excec(self, pg_table, ms_table, service, layerid):
        table = pg_table.lower()
        # Get Columns form PostgreSQL
        columns = pgServer.select_schema(table)
        # Builder Query for PostgreSQL
        pq_query = pgServer.query_builder(columns, table)
        # Select Data with pg_query
        pg_rows = pgServer.select(pq_query)
        # Validate null data
        pg_results = pgServer.validate_data(pg_rows)

        ## MS SQL table name
        # Insert Multiple database to MS SQL
        # msServer.multiple_insert(ms_table, columns, pg_results)
        # Add layername and layerid column | ten service khi publish
        # msServer.update_value_null(ms_table, 'layername', service)
        # value = 'layer_id_them_o_day' | id cua layer
        # msServer.update_value_null(ms_table, 'layerid', layerid)

        ## Rabbit
        Rabbit.modify_array_pg(columns, pg_results, ms_table, service, layerid)



if __name__ == '__main__':
    print 'Flow Processing...'
    FL = FlowProcess()
    pg_table = 'phuonghx_magma3'
    ms_table = 'Tbl_fc_magma'
    service = 'fc_magma_1'
    layerid = 4

    FL.excec(pg_table, ms_table, service, layerid)
