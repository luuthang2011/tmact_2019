import arcpy, sys

sys.path.append(r'E:\SourceCode\tmact_2019\Libs')
import listing_layer
# import file


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
                print gl.name + " " + gl.dataSource
                self.import2db(
                    gl,
                    indb
                )

                # import data to db for CMS
                    # code file import db cho tung table
                    # call


                # end import data to db for CMS

                self.setDataSource(gl)

    def setDataSource (self, gl):
        print gl.name + " " + gl.dataSource


if __name__ == '__main__':
    data = r"E:\SourceCode\tmact_2019\data\gdb\dia_tang_gdb.mxd"
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'
    layer2DB().execute(data, db)
