import arcpy, sys

sys.path.append(r'E:\SourceCode\tmact_2019\Libs')
import listing_layer
# import file
import SQLServer
import PostgresServer


pgServer = PostgresServer.DB('')
msServer = SQLServer.DB('')


class layer2DB:
    def __init__(self):
        print "inited"

    def import2db(self, lyr, db):
        # arcpy.FeatureClassToGeodatabase_conversion(lyr, db)
        # The name contains must not invalid characters (cd: -)
        try:
            arcpy.FeatureClassToFeatureClass_conversion(
                lyr,
                db,
                lyr.name
            )
        except arcpy.ExecuteError, ex:
            print "An error occurred in creating SDE Connection file: " + ex[0]

    def execute(self, indata, indb):
        unitest = listing_layer.listing_layer(indata)
        glayers = unitest.listGroupLayer()
        for gl in glayers:
            if gl.isFeatureLayer:
                print 'Name: ' + gl.name + ", Data Source: " + gl.dataSource
                self.import2db(
                    gl,
                    indb
                )

                # import data to db for CMS

                # Lower table name
                table = gl.name.lower()
                # Get Columns form PostgreSQL
                columns = pgServer.select_schema(table)
                # Builder Query for PostgreSQL
                pq_query = pgServer.query_builder(columns, table)
                # Select Data with pg_query
                pg_rows = pgServer.select(pq_query)
                # Validate null data
                pg_results = pgServer.validate_data(pg_rows)
                # MS SQL table name
                ms_table = 'CSDLTayBac.dbo.Tbl_fc_magma'
                # Insert Multiple database to MS SQL
                # Add layername and layerid column
                # columns += ['layername', 'layerid']
                # print columns
                msServer.multiple_insert(ms_table, columns, pg_results)
                field = 'layername'
                msServer.update_value_null(ms_table, field, 'layer_name_them_o_day')
                field = 'layerid'
                # value = 'layer_id_them_o_day'
                msServer.update_value_null(ms_table, field, 'layer_id_them_o_day')

                # end import data to db for CMS

                self.setDataSource(gl)

    def setDataSource (self, gl):
        print gl.name + " " + gl.dataSource


if __name__ == '__main__':
    data = r"E:\SourceCode\tmact_2019\data\gdb\dia_tang_gdb.mxd"
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'
    layer2DB().execute(data, db)
