import sys, os

dirpath = os.getcwd()
sys.path.append(dirpath + r'\Libs')

import feature2geodatabase
import updateDataSource

class Ks:
    def __init__(self, db, o):
        global sde, objectType
        sde = db
        objectType = o

    def getinput(self, folder):
        scan_folder = os.walk(folder).next()[1]
        scan_file = os.walk(folder).next()[2]
        # print scan_file.__len__() == 1, '*.mxd' in scan_file

        if scan_file.__len__() == 1 and scan_folder.__len__() == 1:
            # mxd, gdb
            return scan_file[0], scan_folder[0]
        else:
            print "Please check mxd + gdb!"
            exit()

    def execute(self, folder):
        # getInput(folder) -> check structure + get mxd
        mxd, gdb = self.getinput(folder)
        mxd = folder + '\\' + mxd
        gdb = folder + '\\' + gdb
        print mxd, gdb

        # feature2geodatabase
        # input: mxd + sde
        # process:
        # - isting_layer: get list layer in mxd
        # - get list feature layer
        # - check all dataSource already exists in Postgres -> if all no:
        # - import gdb to sde: sde.'objectType + dataName + lyr.name' -> if all done
        # - import sde to mssql
        # output:
        # - data in sde + mssql
        feature2db = feature2geodatabase.layer2DB(objectType)
        feature2db.execute(mxd, sde)

        # update layer source from gdb to sde: Libs/updateDataSource.py
        updateSource = updateDataSource.updateDataSource(mxd)
        newmxd = folder + '\\sde_' + mxd
        result = updateSource.execute(gdb,sde)
        result.saveACopy(newmxd)


if __name__ == '__main__':
    objectType = 'CSDLTayBac.dbo.Tbl_fc_magma'
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'

    # python main.py [arg]
    # folder
    print 'Argument List:', str(sys.argv)

    # unitest = Ks(db, objectType)
    # unitest.execute(r'E:\SourceCode\tmact_2019\data\gdb')
