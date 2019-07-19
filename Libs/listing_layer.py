# -*- coding: utf-8 -*-

import arcpy


class listing_layer:
    def __init__(self, in_data):
        global mapDoc
        mapDoc = in_data

    def listGroupLayer(self):
        mxd = arcpy.mapping.MapDocument(mapDoc)
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        layers = arcpy.mapping.ListLayers(df)

        main_layer = layers[0]
        # print main_layer.name

        glayers = arcpy.mapping.ListLayers(main_layer)
        for gl in glayers:
            if not gl.isGroupLayer:
                print gl.name + " " + gl.dataSource

        # for l in layers:
        #     if l.isGroupLayer:
        #         print "isGroupLayer: " + l.name
        #
        #         glayers = arcpy.mapping.ListLayers(l)
        #         for gl in glayers:
        #             if gl.isGroupLayer != True:
        #                 print gl.name
        #                 # apply symbology
        #                 # arcpy.ApplySymbologyFromLayer_management(gl, r"C:\GIS\lyrfiles\mylayersymbology.lyr")
        #
        #         # use as
        #         print "end"


if __name__ == '__main__':
    # in folder ++ "rawdata" || out_table ++ "mediate"
    data = r"E:\SourceCode\tmact_2019\data\gdb\dia_tang_gdb.mxd"

    unitest = listing_layer(data)
    print unitest.listGroupLayer()
