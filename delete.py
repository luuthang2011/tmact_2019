# encoding=utf8
import sys, os
import json
import urllib
import urllib2
import arcpy
import time
from pymongo import MongoClient
sys.path.append(r'E:\SourceCode\tmact_2019\Libs')
reload(sys)
import SQLServer
import flowProcess
import rabbitmq
import listing_layer


class Delete:
    def __init__(self):
        print "inited"
        global msServer, Rabbit

        msServer = SQLServer.DB('')
        Rabbit = rabbitmq.Rabbit()

    def deleteMongo(self, url):
        myclient = MongoClient('mongodb://fimo:fimo!54321@10.101.3.204:27017/ks')
        mydb = myclient["ks"]
        mycol = mydb["map_services"]        # map_services: collection in database
        myquery = {"url": url}
        mycol.delete_one(myquery)

    def gentoken(self, url, username, password, expiration=60):
        query_dict = {'username': username,
                      'password': password,
                      'expiration': str(expiration),
                      'client': 'requestip'}
        query_string = urllib.urlencode(query_dict)
        return json.loads(urllib.urlopen(url + "?f=json", query_string).read())['token']

    def deleteservice(self, server, servicename, username, password, token=None, port=6080):
        if token is None:
            token_url = "http://{}:{}/arcgis/admin/generateToken".format(server, port)
            token = self.gentoken(token_url, username, password)
        delete_service_url = "http://{}:{}/arcgis/admin/services/{}/delete?token={}".format(server, port, servicename,
                                                                                            token)
        urllib2.urlopen(delete_service_url, ' ').read()  # The ' ' forces POST

    def deleteDB(self, mxd):
        listLayer = listing_layer.listing_layer(mxd)
        glayers = listLayer.listGroupLayer()
        # check isFeatureLayer and insert
        for layer in glayers:
            if layer.isFeatureLayer:
                print 'Name: ' + layer.name + ", Data Source: " + layer.dataSource
                arcpy.Delete_management(layer.dataSource)

    def deleteRabbit(self, mxd, ms_table, serviceName):
        listLayer = listing_layer.listing_layer(mxd)
        glayers = listLayer.listGroupLayer()
        # check isFeatureLayer and insert

        for i in range(len(glayers)):
            if glayers[i].isFeatureLayer:
                print 'Name: ' + glayers[i].name + ", Data Source: " + glayers[i].dataSource
                print "Start Delete Rabbit"
                # check isFeatureLayer and insert
                FL = flowProcess.FlowProcess()
                FL.excec(glayers[i].dataSource.split('.')[-1], ms_table, serviceName, i, 'DELETE')


    def deleteMSSQL(self, ms_table, service):
        msServer.delete_row_service(ms_table, 'LayerName', service)

    # def deleteRabbit(self, ms_table, service):
    #     print "Start Delete Rabbit"
    #     # check isFeatureLayer and insert
    #     FL = flowProcess.FlowProcess()
    #     FL.excec(pg_table, ms_table, service, layerid, action)



    def deleteDir(self, folder):
        # os.chmod(folder, 0777)
        os.rename(folder, folder[:-1] + '_deleted_' + str(int(time.time())))


if __name__ == '__main__':
    unitest = Delete()
    # ex: http://<server name>:6080/arcgis/admin
    server = 'localhost'  # fixed
    admin = "fimo"  # fixed
    password = "Mrvm3CVEvr8JGet9"  # fixed

    root = r'E:\SourceCode\tmact_2019\data\gdb\\' # fixed

    print 'Argument List:', str(sys.argv)
    # sys.argv[1] "Tbl_fc_magma_sde_dia_tang_gdb"
    # sys.argv[2] r'E:/SourceCode/tmact_2019/data/gdb/chanqua/'
    # sys.argv[3] r'E:/SourceCode/tmact_2019/data/gdb/chanqua/sde_dia_tang_gdb.mxd'

    # service = "Tbl_fc_magma_sde_dia_tang_gdb"  # from DB
    # service = "Tbl_FC_Magma_sde_dia_tang_gdb"  # from DB
    # folder = r'E:/SourceCode/tmact_2019/data/gdb/chanqua/'
    # mxd = r'E:/SourceCode/tmact_2019/data/gdb/chanqua/sde_dia_tang_gdb.mxd'
    #
    service = sys.argv[1]  # from DB
    folder = sys.argv[2]
    mxd = sys.argv[3]
    ms_table = 'Tbl_FC_Magma'
    # ms_table = sys.argv[4]

    print 'Start delete Rabbit!'
    unitest.deleteRabbit(mxd, ms_table, service)

    # if you need a token, execute this line:

    print 'Start delete MongoDB!'
    unitest.deleteMongo(service)
    print 'Start delete MSSQL!'
    unitest.deleteMSSQL(ms_table, service)

    print 'Start delete Service!'
    unitest.deleteservice(server, service + ".MapServer", admin, password)
    print 'Start delete PostgreDB!'
    unitest.deleteDB(mxd)
    print 'Start delete Directory!'
    unitest.deleteDir(folder)
