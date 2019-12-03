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
        ms_dean = 0
        check_da = ['id_da', 'isdean']
        # table = pg_table
        # Get Columns form PostgreSQL
        columns = pgServer.select_schema(table)

        check_field = all(elem in columns for elem in check_da)

        # pq_query = pgServer.query_builder(columns, table)
        # pq_query = pgServer.query_builder_with_custom_field(columns, table) # Added isDean Field
        if 'rgb_color' in columns: columns.remove('rgb_color') # Remove rgb_color
        if 'red' in columns: columns.remove('red')
        if 'green' in columns: columns.remove('green')
        if 'blue' in columns: columns.remove('blue')
        if check_field:
            print '****************************'
            print 'Contain ID_DA'
            print '****************************'
            # Builder Query for PostgreSQL
            pg_dean = pgServer.query_get_id_dean(table)
            if pg_dean != 0:
                if pg_dean[1] == 1:
                    ms_dean = msServer.select_id_dean(pg_dean[0])
                elif pg_dean[1] == 0:
                    ms_dean = msServer.select_id_luutru(pg_dean[0])

            pq_query = pgServer.query_builder_with_custom_field(ms_dean, columns, table, user, service, layerid) # Added isDean Field
        else:
            print '****************************'
            print 'Not Contain ID_DA'
            print '****************************'
            pq_query = pgServer.query_builder_with_custom_field_whitout_id_dean(columns, table, user, service,
                                                                layerid)  # Added isDean Field
        # Select Data with pg_query
        pg_rows = pgServer.select(pq_query)
        # Validate null data
        pg_validate_rows = pgServer.validate_data(pg_rows)

        columns_custom = columns[:]
        # print columns
        if check_field:
            columns_custom.append('ID_DA')

        columns_custom.append('CreatedDate')
        columns_custom.append('UpdatedDate')

        columns_custom.append('CreatedBy')
        columns_custom.append('UpdatedBy')
        columns_custom.append('LayerName')
        columns_custom.append('LayerID')

        # columns_custom.append('CreatedBy')
        # columns_custom.append('UpdatedBy')

        # columns_custom.append('isDean')

        if action == 'CREATE':
            ## MS SQL table name
            # Insert Multiple database to MS SQL

            msServer.multiple_insert(ms_table, columns_custom, pg_validate_rows)

            if 'id' not in columns_custom: columns_custom.append('id')
            ms_rows = msServer.select(ms_table, columns_custom, service, layerid)

            ## Rabbit create json
            print 'Create FLow'
            # print pg_validate_rows
            # strRabbit = Rabbit.modify_array_pg(columns, pg_validate_rows, ms_table, service, layerid, 'CREATE')
            # strRabbit = Rabbit.modify_array_pg(columns_custom, pg_validate_rows, ms_table, service, layerid, user, 'CREATE')
            strRabbit = Rabbit.modify_array_pg(columns_custom, ms_rows, ms_table, service, layerid, user, 'CREATE')
            Rabbit.create_json(strRabbit)
        elif action == 'DELETE':
            # strRabbit = Rabbit.modify_array_pg(columns, pg_validate_rows, ms_table, service, layerid, 'DELETE')
            # strRabbit = Rabbit.modify_array_pg(columns_custom, pg_validate_rows, ms_table, service, layerid, user, 'DELETE')
            if 'id' not in columns_custom: columns_custom.append('id')
            ms_rows = msServer.select(ms_table, columns_custom, service, layerid)
            strRabbit = Rabbit.modify_array_pg(columns_custom, ms_rows, ms_table, service, layerid, user, 'DELETE')
            Rabbit.delete_json(strRabbit)


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

