# encoding=utf8
import sys, os
sys.path.append(r'E:\SourceCode\tmact_2019\Libs')
reload(sys)
sys.setdefaultencoding('utf8')

import feature2geodatabase
import updateDataSource
import publish_mapService_from_mapDocument
import listing_layer
import flowProcess
import delete

class Ks:
    def __init__(self, db, o, staticAgs):
        global sde, objectType, ags
        sde = db
        objectType = o
        ags = staticAgs

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
        mxd_print = folder + '\\' + mxd
        gdb_print = folder + '\\' + gdb
        print mxd_print, gdb_print

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
        feature2db = feature2geodatabase.layer2DB()
        feature2db.execute(mxd_print, sde)

        # update layer source from gdb to sde: Libs/updateDataSource.py
        updateSource = updateDataSource.updateDataSource(mxd_print)
        newmxd = folder + '\\sde_' + mxd

        # print "mxd_print" + mxd_print + "gdb_print" + gdb_print + "newmxd" + newmxd
        result = updateSource.execute(gdb_print,sde)
        result.saveACopy(newmxd)

        # publish service to map server
        # rewritable: true
        serviceName = objectType + '_sde_' + mxd[:-4]
        print 'serviceName:' + serviceName
        publisher = publish_mapService_from_mapDocument.publish_mapService_from_mapDocument(
            folder,
            newmxd,
            ags,
            serviceName
            # "ahihi"
        )
        iscompleted = publisher.execute()

        # insert db to MS SQL
        # listing layer from sde mxd file
        listLayer = listing_layer.listing_layer(newmxd)
        glayers = listLayer.listGroupLayer()

        if iscompleted:
            # check isFeatureLayer and insert
            FL = flowProcess.FlowProcess()

            for i in range(len(glayers)):
                if glayers[i].isFeatureLayer:
                    print 'Name: ' + glayers[i].name + ", Data Source: " + glayers[i].dataSource
                    print glayers[i].dataSource.split('.')[-1]
                    print objectType
                    print serviceName
                    print i
                    # FL.excec(glayers[i].dataSource.split('.')[-1], objectType, serviceName, i)
        else:
            deleter = delete.Delete()
            deleter.deleteDB(newmxd)


if __name__ == '__main__':
    staticAgs = r"E:\SourceCode\tmact_2019\data\connect_information\ArcgisPublishServer.ags"
    db = r'E:\SourceCode\tmact_2019\data\connect_information\ks_connection.sde'

    # python main.py [arg]
    # folder
    print 'Argument List:', str(sys.argv)

    objectType = 'Tbl_fc_magma'
    # objectType = sys.argv[1]
    folder = r'E:/SourceCode/tmact_2019/data/gdb/chanqua/'
    # folder = sys.argv[2]

    unitest = Ks(db, objectType, staticAgs)
    unitest.execute(folder)
