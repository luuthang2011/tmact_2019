import sys, delete, constant, time
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

if __name__ == '__main__':
    try:
        unitest = delete.Delete()
        # ex: http://<server name>:6080/arcgis/admin
        server = constant.server  # fixed
        admin = constant.admin  # fixed
        password = constant.password  # fixed

        # root = r'E:\SourceCode\tmact_2019\data\mdb\\' # fixed

        print 'Argument List:', str(sys.argv)

        # service = "Magma"  # from DB
        # folder = r'E:/SourceCode/tmact_2019/data/mdb/Magma/'
        # mxd = r'E:/SourceCode/tmact_2019/data/mdb/Magma/prepare.mxd'
        # ms_table = 'Tbl_FC_Magma'

        service = sys.argv[1]  # from DB
        folder = sys.argv[2]
        mxd = sys.argv[3]
        ms_table = sys.argv[4]

        try:
            print 'Start delete Rabbit!'
            unitest.deleteRabbit(mxd, ms_table, service)
            time.sleep(1)

            # if you need a token, execute this line:
            print 'Start delete MSSQL!'
            unitest.deleteMSSQL(ms_table, service)
        except Exception, e:
            print("An exception occurred in delete rabbit or mssql")
            print e.message

        print 'Start delete Service!'
        unitest.deleteservice(server, service + ".MapServer", admin, password)
        time.sleep(4)

        print 'Start delete PostgreDB!'
        unitest.deleteDB(mxd)

        # print 'Start delete Directory!'
        # unitest.deleteDir(folder)
        print 'Start delete MongoDB!'
        unitest.deleteMongo(service)
        print 'All done'

    except Exception, e:
        print("An exception occurred in delete spatial data")
        print e.message
        print "----------------------------------------------"
        print "----Flow end. Exception. Pls check errors!----"
        print "----------------------------------------------"
