# Name: FeatureClassToGeodatabase_Example2.py
# Description: Use FeatureClassToGeodatabase to copy feature classes
#  to geodatabase format

# Import modules
import arcpy

# # Set environment settings
# arcpy.env.workspace = r'E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132.mdb'
#
# # Set local variables
# inFeatures = ['FC_Magma_Bd132']
# outLocation = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'
#
# # Execute TableToGeodatabase
# arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)


# newmxd = arcpy.mapping.MapDocument(r"E:\SourceCode\tmact_2019\data\gdb\magma3layer\main.mxd")
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
            r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde',               # out_path
            lyr.datasetName     # datasetName
        )