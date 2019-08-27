# encoding=utf8
import sys, os
import json
import urllib
import urllib2
import arcpy
import time
from pymongo import MongoClient

sys.path.append(r'E:\SourceCode\tmact_2019\Libs')
import listing_layer


class Delete:
    def __init__(self):
        print "inited"

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

    def deleteMSSQL(self, mxd):
        listLayer = listing_layer.listing_layer(mxd)
        glayers = listLayer.listGroupLayer()
        # check isFeatureLayer and insert
        for layer in glayers:
            if layer.isFeatureLayer:
                print 'Name: ' + layer.name + ", Data Source: " + layer.dataSource
                # arcpy.Delete_management(layer.dataSource)

    def deleteDir(self, root, folder):
        # os.chmod(folder, 0777)
        os.rename(root + folder, root + 'deleted_' + folder + '_' + str(int(time.time())))


if __name__ == '__main__':
    unitest = Delete()
    # ex: http://<server name>:6080/arcgis/admin
    server = 'localhost'  # fixed
    admin = "fimo"  # fixed
    password = "Mrvm3CVEvr8JGet9"  # fixed

    root = r'E:\SourceCode\tmact_2019\data\gdb\\'
    service = "Tbl_fc_magma_sde_dia_tang_gdb"  # from DB
    folder = r'chanqua'
    mxd = r'E:\SourceCode\tmact_2019\data\gdb\chanqua\sde_dia_tang_gdb.mxd'

    # if you need a token, execute this line:
    unitest.deleteservice(server, service + ".MapServer", admin, password)
    unitest.deleteDB(mxd)
    unitest.deleteDir(root, folder)
    unitest.deleteMongo(service)
    # unitest.deleteMQSQL()
    # unitest.deleteElastic()