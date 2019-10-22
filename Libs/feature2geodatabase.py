import arcpy


class layer2DB:
    def __init__(self, db):
        global indb
        indb = db

    def execute(self, indata, mdb):
        # Set the current workspace
        arcpy.env.workspace = indb

        # read mxd
        # input: mxd path
        # out: list layer
        mxd = arcpy.mapping.MapDocument(indata)

        # check exists in geoDatabase
        # input: isFeatureLayer lyr
        # out: true
        # false: exit
        print "start check database"
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.supports("DATASOURCE"):
                print lyr.name
                if arcpy.Exists(lyr.datasetName):
                    print lyr.name + " already exists in geoDatabase"
                    exit()

        # correct data source
        # input: mxd variable
        # out: update mxd variable
        mxd.findAndReplaceWorkspacePaths("", mdb, False)

        mxd.saveACopy(r"E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132_final_formated_new.mxd")

        newmxd = arcpy.mapping.MapDocument(r"E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132_final_formated_new.mxd")

        # export data to db
        # input:  updated mxd variable
        # output:  none
        print "start export data to database"
        for lyr in arcpy.mapping.ListLayers(newmxd):
            if lyr.isFeatureLayer:
                print lyr.name
                print lyr.datasetName
                print lyr.dataSource
                print lyr.isFeatureLayer
                arcpy.FeatureClassToFeatureClass_conversion(
                    lyr,                # in_features
                    indb,               # out_path
                    lyr.datasetName     # datasetName
                )
                # lyr.saveACopy(r"E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132_final_formated_new.lyr")

        # df = arcpy.mapping.ListDataFrames(mxd)[0]
        # layers = arcpy.mapping.ListLayers(df)
        # main_layer = layers[0]
        # glayers = arcpy.mapping.ListLayers(main_layer)
        # for scanLayer in glayers:
        #     if scanLayer.isFeatureLayer:
        #         print scanLayer.name
        #         print scanLayer.datasetName
        #         print scanLayer.dataSource
        #         print scanLayer.isFeatureLayer
        #         arcpy.FeatureClassToFeatureClass_conversion(
        #             scanLayer,                # in_features
        #             indb,               # out_path
        #             scanLayer.datasetName     # datasetName
        #         )


if __name__ == '__main__':
    data = r"E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132_final_formated.mxd"
    mdb = r"E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132.mdb"
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'
    layer2DB(db).execute(data, mdb)
