# -*- coding: utf-8 -*-

import arcpy


class listing_layer:
    def __init__(self, in_data):
        global mapDoc
        mapDoc = in_data

    def listGroupLayer(self):
        mxd = arcpy.mapping.MapDocument(mapDoc)
        # df = arcpy.mapping.ListDataFrames(mxd)[0]
        # layers = arcpy.mapping.ListLayers(df)
        #
        # main_layer = layers[0]
        # # print main_layer.name
        #
        # glayers = arcpy.mapping.ListLayers(main_layer)

        return arcpy.mapping.ListLayers(mxd)


if __name__ == '__main__':
    # in folder ++ "rawdata" || out_table ++ "mediate"
    data = r"E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132_final_formated.mxd"

    unitest = listing_layer(data)
    print unitest.listGroupLayer()
