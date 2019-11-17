# -*- coding: utf-8 -*-

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

    def excec(self, pg_table, ms_table, service, layerid, user, action):
        table = pg_table.lower()
        # table = pg_table
        # Get Columns form PostgreSQL
        columns = pgServer.select_schema(table)
        # Builder Query for PostgreSQL

        pg_dean = pgServer.query_get_id_dean(table)
        ms_dean = msServer.select_id_dean(pg_dean)

        # pq_query = pgServer.query_builder(columns, table)
        # pq_query = pgServer.query_builder_with_custom_field(columns, table) # Added isDean Field
        pq_query = pgServer.query_builder_with_custom_field(ms_dean, columns, table, user, service, layerid) # Added isDean Field
        # Select Data with pg_query
        pg_rows = pgServer.select(pq_query)
        # Validate null data
        pg_validate_rows = pgServer.validate_data(pg_rows)
        # disconnect DB
        # pgServer.cursor.close()
        # pgServer.connection.close()

        columns_custom = columns[:]
        # print columns
        columns_custom.append('ID_DA')
        columns_custom.append('CreatedDate')
        columns_custom.append('UpdatedDate')

        columns_custom.append('CreatedBy')
        columns_custom.append('UpdatedBy')
        columns_custom.append('LayerName')
        columns_custom.append('LayerID')

        if 'rgb_color' in columns_custom: columns_custom.remove('rgb_color')
        if 'red' in columns_custom: columns_custom.remove('red')
        if 'green' in columns_custom: columns_custom.remove('green')
        if 'blue' in columns_custom: columns_custom.remove('blue')
        # columns_custom.append('CreatedBy')
        # columns_custom.append('UpdatedBy')

        # columns_custom.append('isDean')

        if action == 'CREATE':
            ## MS SQL table name
            # Insert Multiple database to MS SQL

            # msServer.multiple_insert(ms_table, columns, pg_validate_rows)
            msServer.multiple_insert(ms_table, columns_custom, pg_validate_rows)
            # Add layername and layerid column | ten service khi publish
            # msServer.update_value_null(ms_table, 'layername', service)
            # value = 'layer_id_them_o_day' | id cua layer
            # msServer.update_value_null(ms_table, 'layerid', layerid)
            # User: [CreatedBy], [UpdatedBy]
            # msServer.update_value_null(ms_table, 'createdby', user)
            # msServer.update_value_null(ms_table, 'updatedby', user)
            ## Rabbit create json
            print 'Create FLow'
            # strRabbit = Rabbit.modify_array_pg(columns, pg_validate_rows, ms_table, service, layerid, 'CREATE')
            strRabbit = Rabbit.modify_array_pg(columns_custom, pg_validate_rows, ms_table, service, layerid, user, 'CREATE')
            Rabbit.create_json(strRabbit)
        elif action == 'DELETE':
            # strRabbit = Rabbit.modify_array_pg(columns, pg_validate_rows, ms_table, service, layerid, 'DELETE')
            strRabbit = Rabbit.modify_array_pg(columns_custom, pg_validate_rows, ms_table, service, layerid, user, 'DELETE')
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

    # pg_table = 'fc_magma_bd132'
    pg_table = 'Bd153'
    ms_table = 'Tbl_FC_TramTich'
    service = 'TramTich'
    layerid = 0
    user = 'PhuongHX'

    FL.excec(pg_table, ms_table, service, layerid, user, "CREATE")
    # FL.excec(pg_table, ms_table, service, layerid, user, "DELETE")

