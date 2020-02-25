import arcpy


class layer2DB:
    def __init__(self, db):
        global indb
        indb = db

    def import2db(self, lyr):
        try:
            arcpy.FeatureClassToFeatureClass_conversion(
                lyr,  # in_features
                indb,  # out_path
                lyr.datasetName  # datasetName
            )
        except arcpy.ExecuteError, ex:
            print "An error occurred in creating SDE Connection file: " + ex[0]
            # exit()

    def execute(self, indata, mdb):
        # Set the current workspace
        arcpy.env.workspace = indb
        arcpy.env.outputZFlag = 'Disabled'
        arcpy.env.outputMFlag = 'Disabled'

        # read mxd
        # input: mxd path
        # out: list layer
        mxd = arcpy.mapping.MapDocument(indata)

        # check exists in geoDatabase
        # input: isFeatureLayer lyr
        # out: true
        # false: exit
        print "start check database"
        sdeList = arcpy.ListFeatureClasses()

        # remove prefix: ks.sde
        for i, magician in enumerate(sdeList):
            sdeList[i] = sdeList[i].split(".")[-1]

        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.isFeatureLayer:
                print lyr.name
                print lyr.datasetName
                if lyr.datasetName in sdeList:
                    print lyr.name + " already exists in geoDatabase"
                    exit()

        # correct data source
        # input: mxd variable
        # out: update mxd variable
        mxd.findAndReplaceWorkspacePaths("", mdb, False)

        # export data to db
        # input:  updated mxd variable
        # output:  none
        print "start export data to database"
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.isFeatureLayer:
                print lyr.name
                print lyr.datasetName
                self.import2db(lyr)


if __name__ == '__main__':
    data = r"E:\SourceCode\tmact_2019\data\mdb\TramTich_Gop.mxd"
    mdb = r"E:\SourceCode\tmact_2019\data\mdb\TramTich_Gop.mdb"
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'
    layer2DB(db).execute(data, mdb)
