# encoding=utf8
import sys, os
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

from pymongo import MongoClient
import feature2geodatabase
import updateDataSource
import publish_mapService_from_mapDocument
import listing_layer
import flowProcess
import delete
import constant


class Ks:
    # check and get input
    # input: folder
    # true: mxd path, mdb path
    # else: exit
    def getinput(self, folder):
        mxdPath = mdbPath = ""

        scan_folder = os.walk(folder).next()[1]
        scan_file = os.walk(folder).next()[2]

        if scan_file.__len__() == 2:
            for file in scan_file:
                if file.endswith(".mxd"):
                    mxdPath = file
                if file.endswith(".mdb"):
                    mdbPath = file
            return mxdPath, mdbPath
        else:
            print "Please check mxd + mdb!"
            exit()

    def importMongo(self, url, ms_table, de_an, folder, mxd):
        client = MongoClient(constant.Mongo)
        db = client['ks']
        post = {
            "url": url,
            "ms_table": ms_table,
            "de_an": de_an,
            "folder": folder,
            "mxd": mxd,
            "visible": 0,
            "opacity": 0.7
        }

        posts = db.map_services  # map_services: collection in database
        post_id = posts.insert_one(post).inserted_id
        print post_id

    def publish(self, folder, sde, staticAgs, objectType):
        # get name and join path
        mxdPath, mdbPath = self.getinput(folder)
        mxdPath = folder + mxdPath
        mdbPath = folder + mdbPath
        print mxdPath, mdbPath

        # feature2geodatabase
        # input: mxd path, mdb path, db_connect
        # out: data already on db
        feature2db = feature2geodatabase.layer2DB(sde)
        feature2db.execute(mxdPath, mdbPath)

        # update data srouce
        # input: mxd
        # output: new mxd
        newMxdPath = folder + 'prepare.mxd'
        updateSource = updateDataSource.updateDataSource(mxdPath)
        newMxdData = updateSource.mdb2sde(sde)
        newMxdData.saveACopy(newMxdPath)

        # publish service
        # input: newMxdPath, AGS file
        # true: done
        # false: delete geodatabase
        serviceName = objectType
        publisher = publish_mapService_from_mapDocument.publish_mapService_from_mapDocument(
            folder,
            newMxdPath,
            staticAgs,
            serviceName
        )
        return publisher.execute()


if __name__ == '__main__':
    staticAgs = constant.staticAgs
    db = constant.db

    # table = sys.argv[1]
    # folder = sys.argv[2]
    # user = sys.argv[3]

    folder = r"E:/SourceCode/tmact_2019/data/mdb/tramtich/"
    table = "Tbl_FC_TramTich"
    user = "from tmact"

    objectType = table.split("_")[-1]       # magma

    try:
        unitest = Ks()
        result = unitest.publish(folder, db, staticAgs, objectType)
        if result:
            print "Published map service!!!!"
            unitest.importMongo(objectType, table, "de_an", folder, folder + 'prepare.mxd')

            # insert db to MS SQL
            # listing layer from sde mxd file
            listLayer = listing_layer.listing_layer(folder + 'prepare.mxd')
            glayers = listLayer.listGroupLayer()

            # check isFeatureLayer and insert
            FL = flowProcess.FlowProcess()

            print "--------Publish end!-----------"

            for i in range(len(glayers)):
                if glayers[i].isFeatureLayer:
                    print 'Name: ' + glayers[i].name + ", Data Source: " + glayers[i].dataSource
                    print glayers[i].dataSource.split('.')[-1]
                    print objectType
                    print table
                    print i
                    print "----------------------------------------------"
                    print "Exec Flow Process"
                    print "----------------------------------------------"
                    FL.excec(glayers[i].dataSource.split('.')[-1], table, objectType, i, user, 'CREATE')
                    print "----------------------------------------------"
                    print "-------------All Done!------------------------"
                    print "----------------------------------------------"
        else:
            print "error"
            deleter = delete.Delete()
            deleter.deleteDB(folder + 'prepare.mxd')
            print "----------------------------------------------"
            print "--Flow end. Publish false. Pls check errors!--"
            print "----------------------------------------------"
    except Exception, e:
        print("An exception occurred")
        print e.message
        deleter = delete.Delete()
        deleter.deleteDB(folder + 'prepare.mxd')
        print "----------------------------------------------"
        print "----Flow end. Exception. Pls check errors!----"
        print "----------------------------------------------"
