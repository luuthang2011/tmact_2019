import sys, delete, constant

if __name__ == '__main__':
    unitest = delete.Delete()
    # ex: http://<server name>:6080/arcgis/admin
    server = constant.server  # fixed
    admin = constant.admin  # fixed
    password = constant.password  # fixed

    # root = r'E:\SourceCode\tmact_2019\data\mdb\\' # fixed

    print 'Argument List:', str(sys.argv)

    # service = "Magma"  # from DB
    # folder = r'E:/SourceCode/tmact_2019/data/mdb/1572371062527/'
    # mxd = r'E:/SourceCode/tmact_2019/data/mdb/1572371062527/prepare.mxd'
    # ms_table = 'Tbl_FC_Magma'

    service = sys.argv[1]  # from DB
    folder = sys.argv[2]
    mxd = sys.argv[3]
    ms_table = sys.argv[4]

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
    # print 'Start delete Directory!'
    # unitest.deleteDir(folder)
    print 'All done'