import SQLServer
import PostgresServer

pgServer = PostgresServer.DB('')
msServer = SQLServer.DB('')


class FlowProcess:
    def __init__(self):
        print 'Init Process'

    def excec(self, pg_table, ms_table, layername, layerid):
        table = pg_table.lower()
        # Get Columns form PostgreSQL
        columns = pgServer.select_schema(table)
        # Builder Query for PostgreSQL
        pq_query = pgServer.query_builder(columns, table)
        # Select Data with pg_query
        pg_rows = pgServer.select(pq_query)
        # Validate null data
        pg_results = pgServer.validate_data(pg_rows)
        # MS SQL table name
        # ms_table = 'CSDLTayBac.dbo.Tbl_fc_magma'
        # Insert Multiple database to MS SQL
        msServer.multiple_insert(ms_table, columns, pg_results)
        # Add layername and layerid column | ten service khi publish
        msServer.update_value_null(ms_table, 'layername', layername)
        # value = 'layer_id_them_o_day' | id cua layer
        msServer.update_value_null(ms_table, 'layerid', layerid)


if __name__ == '__main__':
    print 'Flow Processing...'
    FL = FlowProcess()
    pg_table = 'f_48_94_c_chu_dt_region'
    ms_table = 'CSDLTayBac.dbo.Tbl_fc_magma'
    layername = 'gia_tri_cua_layer_name'
    layerid = 'gia_tri_cua_layer_id'

    FL.excec(pg_table, ms_table, layername, layerid)
