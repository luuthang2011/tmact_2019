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

    def excec(self, pg_table, ms_table, service, layerid, action):
        table = pg_table.lower()
        # Get Columns form PostgreSQL
        columns = pgServer.select_schema(table)
        # Builder Query for PostgreSQL
        pq_query = pgServer.query_builder(columns, table)
        # Select Data with pg_query
        pg_rows = pgServer.select(pq_query)
        # Validate null data
        pg_validate_rows = pgServer.validate_data(pg_rows)

        ## MS SQL table name
        # Insert Multiple database to MS SQL
        msServer.multiple_insert(ms_table, columns, pg_validate_rows)
        # Add layername and layerid column | ten service khi publish
        msServer.update_value_null(ms_table, 'layername', service)
        # value = 'layer_id_them_o_day' | id cua layer
        msServer.update_value_null(ms_table, 'layerid', layerid)

        if action == 'CREATE':
            ## Rabbit create json
            print 'Create FLow'
            strRabbit = Rabbit.modify_array_pg(columns, pg_validate_rows, ms_table, service, layerid, 'CREATE')
            Rabbit.create_json(strRabbit)
        elif action == 'DELETE':
            strRabbit = Rabbit.modify_array_pg(columns, pg_validate_rows, ms_table, service, layerid, 'DELETE')
            Rabbit.delete_json(strRabbit)


    # def delete(self, pg_table, ms_table, service, layerid):
        # strRabbit = Rabbit.modify_array_pg(columns, pg_validate_rows, ms_table, service, layerid, 'DELETE')
        # Rabbit.delete_json(strRabbit)


if __name__ == '__main__':
    print 'Flow Processing...'
    FL = FlowProcess()
    # pg_table = 'phuonghx_magma3'
    # ms_table = 'Tbl_fc_magma'
    # service = 'fc_magma_1'
    # layerid = 4

    pg_table = 'F_48_94_C_Chu_DT_region'
    ms_table = 'Tbl_fc_magma'
    service = 'Tbl_fc_magma_sde_dia_tang_gdb'
    layerid = 2

    FL.excec(pg_table, ms_table, service, layerid, "CREATE")

