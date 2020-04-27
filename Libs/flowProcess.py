# -*- coding: utf-8 -*-

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

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
        check_da = ['isdean', 'id_da']
        is_da = 1
        # table = pg_table
        # Get Columns form PostgreSQL
        columns = pgServer.select_schema(table)

        pq_query = pgServer.query_builder_with_custom_field(columns, table, user, service,
                                                            layerid)  # Added isDean Field

        # Select Data with pg_query
        pg_rows = pgServer.select(pq_query)
        # print pg_rows
        # Validate null data
        pg_validate_rows = pgServer.validate_data(pg_rows)

        columns_custom = columns[:]
        # print columns

        # if check_field:
        #     columns_custom.append('ID_DA')

        columns_custom.append('CreatedDate')
        columns_custom.append('UpdatedDate')

        columns_custom.append('CreatedBy')
        columns_custom.append('UpdatedBy')
        columns_custom.append('LayerName')
        columns_custom.append('LayerID')

        if action == 'CREATE':
            ## MS SQL table name
            # Insert Multiple database to MS SQL
            print 'pg_table: %s' % table
            msServer.multiple_insert(ms_table, columns_custom, pg_validate_rows, is_da)
            if 'id' not in columns_custom: columns_custom.append('id')
            ms_rows = msServer.select(ms_table, columns_custom, service, layerid)

            ## Rabbit create json
            print 'Create FLow'
            strRabbit = Rabbit.modify_array_pg(columns_custom, ms_rows, ms_table, service, layerid, user, 'CREATE')
            Rabbit.create_json(strRabbit)
        elif action == 'DELETE':
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

    # pg_table = 'Bd153'
    # ms_table = 'Tbl_FC_TramTich'
    # service = 'TramTich'
    # layerid = 0
    # user = 'PhuongHX'

    # ks.sde.KSnhoLe_region
    # pg_table = 'KSnhoLe_region'
    # ms_table = 'Tbl_FC_Khoangsannhole'
    # service = 'Khoangsannhole'
    # layerid = 0
    # user = 'PhuongHX'

    pg_table = 'TramTich_DaiThi_PhiaKhao_Bd132'
    ms_table = 'Tbl_FC_TramTich'
    service = 'TramTich'

    # pg_table = 'TramTich_DaiThi_PhiaKhao_Bd132'
    # ms_table = 'Tbl_FC_TramTich'
    # service = 'TramTich'


    layerid = 0
    user = 'From TMACT'

    FL.excec(pg_table, ms_table, service, layerid, user, "CREATE")
    # FL.excec(pg_table, ms_table, service, layerid, user, "DELETE")

