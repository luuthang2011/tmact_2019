import arcpy


class updateDataSource:
    def __init__(self, inMXD):
        global mxd
        mxd = mxd = arcpy.mapping.MapDocument(inMXD)

    def execute(self, inGDB, outSDE):
        mxd.replaceWorkspaces (inGDB, "FILEGDB_WORKSPACE", outSDE, "SDE_WORKSPACE")
        print 'update source completed'
        return mxd


if __name__ == '__main__':
    unitest = updateDataSource(r"E:\SourceCode\tmact_2019\data\gdb\gdb\dia_tang_gdb.mxd")
    result = unitest.execute(
        r"E:\SourceCode\tmact_2019\data\gdb\gdb\ks.gdb",
        r"E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde"
    )
    result.saveACopy(r"E:\SourceCode\tmact_2019\data\gdb\gdb\sde_dia_tang_gdb.mxd")
    print "done"