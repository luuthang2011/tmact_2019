# findAndReplaceWorkspacePaths (find_workspace_path, replace_workspace_path, {validate})
# Parameter	Explanation	Data Type
# find_workspace_path
# A string that represents the workspace path or connection file you want to find. If an empty string is passed, then all workspace paths will be replaced with the replace_workspace_path, depending on the value of the validate parameter.
#
# String
# replace_workspace_path
# A string that represents the workspace path or connection file you want to use to replace.
#
# String
# validate
# If set to True, a workspace will only be updated if the replace_workspace_path value is a valid workspace. If it is not valid, the workspace will not be replaced. If set to False, the method will set all workspaces to match the replace_workspace_path, regardless of a valid match. In this case, if a match does not exist, then the layer and table's data sources would be broken.
#
# (The default value is True)
#
# Boolean

import arcpy


class updateDataSource:
    def __init__(self, inMXD):
        global mxd
        mxd = mxd = arcpy.mapping.MapDocument(inMXD)

    def execute(self, inGDB, outSDE):
        mxd.replaceWorkspaces (inGDB, "ACCESS_WORKSPACE", outSDE, "SDE_WORKSPACE")
        print 'update source completed'
        return mxd

    def mdb2sde(self, outSDE):
        mxd.replaceWorkspaces ("", "", outSDE, "SDE_WORKSPACE", False)
        print 'update source completed'
        return mxd

    def mdb2sdeLocal(self, outGDB):
        mxd.replaceWorkspaces ("", "", outGDB, "ACCESS_WORKSPACE", False)
        print 'update source completed'
        return mxd


if __name__ == '__main__':
    unitest = updateDataSource(r"E:\SourceCode\tmact_2019\data\mdb\DutGay.10.3.mxd")
    # result = unitest.execute(
    #     r"E:\SourceCode\tmact_2019\data\mdb\magma-2019-10-22\FC_Magma_Bd132.mdb",
    #     r"E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde"
    # )

    unitest.mdb2sdeLocal(r"E:\SourceCode\tmact_2019\data\mdb\DutGay_Gop.mdb")
    result = unitest.mdb2sde(r"E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde")
    result.saveACopy(r"E:\SourceCode\tmact_2019\data\mdb\DutGay.10.3.new.mxd")
    print "done"