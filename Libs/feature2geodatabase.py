import arcpy

# sys.path.append(r'E:\SourceCode\tmact_2019\Libs')
import listing_layer


class layer2DB:
    def __init__(self, o):
        global objectType, dataName
        # objectType: loai doi tuong ban do = mssql table name
        # dataName: mxd file name
        objectType = o
        # dataName = d
        # print "inited"

    def import2db(self, lyr, db):
        # arcpy.FeatureClassToGeodatabase_conversion(lyr, db)
        # The name contains must not invalid characters (cd: -)
        # try:
        #     arcpy.FeatureClassToFeatureClass_conversion(
        #         lyr,  # in_features
        #         db,  # out_path
        #         lyr.name  # out_name
        #     )
        # except arcpy.ExecuteError, ex:
        #     print "An error occurred in creating SDE Connection file: " + ex[0]
        arcpy.FeatureClassToFeatureClass_conversion(
            lyr,  # in_features
            db,  # out_path
            lyr.name  # out_name
        )

    def execute(self, indata, indb):
        unitest = listing_layer.listing_layer(indata)
        glayers = unitest.listGroupLayer()

        # Set the current workspace
        arcpy.env.workspace = indb
        for gl in glayers:
            if gl.isFeatureLayer:
                print 'Name: ' + gl.name + ", Data Source: " + gl.dataSource
                if arcpy.Exists(gl.name):
                    print gl.name + " already exists in geoDatabase"
                    exit()

        for gl in glayers:
            if gl.isFeatureLayer:
                # gl.name: F_48_94_C_Chu_DT_region
                # gl.dataSource: E:\SourceCode\tmact_2019\data\gdb\ks.gdb\F_48_94_C_Chu_DT_region
                self.import2db(
                    gl,
                    indb
                )

        # import data to db for CMS after import2db all completed
        for gl in glayers:
            if gl.isFeatureLayer:
                try:
                    # Flow process ???
                    print 'Start Flow Process???'

                    # end import data to db for CMS
                except:
                    print("Something went wrong when import data to CSM's database")

                # self.setDataSource(gl)

    def setDataSource(self, gl):
        print gl.name + " " + gl.dataSource


if __name__ == '__main__':
    objectType = 'CSDLTayBac.dbo.Tbl_fc_magma'
    # dataName = 'dia_tang'
    data = r"E:\SourceCode\tmact_2019\data\gdb\dia_tang_gdb.mxd"
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'
    layer2DB(objectType).execute(data, db)
