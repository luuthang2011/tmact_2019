import arcpy
import listing_layer
from pathlib import *


class layer2DB:
    def __init__(self):
        print "inited"

    def import2db(self, lyr, db):
        # arcpy.FeatureClassToGeodatabase_conversion(lyr, db)
        # The name contains must not invalid characters (cd: -)
        try:
            arcpy.FeatureClassToFeatureClass_conversion(
                lyr,  # in_features
                db,  # out_path
                lyr.dataSource.split("\\")[-1]  # out_name
            )
        except arcpy.ExecuteError, ex:
            print "An error occurred in creating SDE Connection file: " + ex[0]
            exit()

    def execute(self, indata, indb):
        unitest = listing_layer.listing_layer(indata)
        glayers = unitest.listGroupLayer()
        pIndata = Path(indata)
        allsource = ""

        # Set the current workspace
        arcpy.env.workspace = indb
        for gl in glayers:
            if gl.isFeatureLayer:
                p = Path(gl.dataSource)

                print gl.dataSource
                allsource = str(p.parent)
                if arcpy.Exists(p.name):
                    print p.name + " already exists in geoDatabase"
                    return False
                else:
                    print "change database source"
                    gl.replaceDataSource(
                        str(pIndata.parent) + "\\" + gl.dataSource.split("\\")[-2],
                        "FILEGDB_WORKSPACE"
                    )
                    print gl.dataSource

        for gl in glayers:
            if gl.isFeatureLayer:
                # gl.name: F_48_94_C_Chu_DT_region
                # gl.dataSource: E:\SourceCode\tmact_2019\data\gdb\ks.gdb\F_48_94_C_Chu_DT_region
                self.import2db(
                    gl,
                    indb
                )

        return allsource

    def setDataSource(self, gl):
        print gl.name + " " + gl.dataSource


if __name__ == '__main__':
    data = r"E:\SourceCode\tmact_2019\data\gdb\magma3layer - Copy\sde_main.mxd"
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'
    layer2DB().execute(data, db)
