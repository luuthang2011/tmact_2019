import sys, delete, constant
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

if __name__ == '__main__':
    unitest = delete.Delete()
    # ex: http://<server name>:6080/arcgis/admin
    server = constant.server  # fixed
    admin = constant.admin  # fixed
    password = constant.password  # fixed

    # root = r'E:\SourceCode\tmact_2019\data\mdb\\' # fixed

    print 'Argument List:', str(sys.argv)

    # service = "DutGay"  # from DB
    # folder = r'E:/SourceCode/tmact_2019/data/mdb/Dutgay3/'
    # mxd = r'E:/SourceCode/tmact_2019/data/mdb/Dutgay3/prepare.mxd'
    # ms_table = 'Tbl_FC_DutGay'

    # service = "BienChat"  # from DB
    # folder = r'E:/SourceCode/tmact_2019/data/mdb/BienChatNew/'
    # mxd = r'E:/SourceCode/tmact_2019/data/mdb/BienChatNew/prepare.mxd'
    # ms_table = 'Tbl_FC_BienChat'

    # service = sys.argv[1]  # from DB
    # folder = sys.argv[2]
    # mxd = sys.argv[3]
    # ms_table = sys.argv[4]

    try:
        print 'Start delete Rabbit!'
        unitest.deleteRabbit(mxd, ms_table, service)

        # if you need a token, execute this line:

        print 'Start delete MSSQL!'
        unitest.deleteMSSQL(ms_table, service)
    except Exception, e:
        print("An exception occurred")
        print e.message

    print 'Start delete Service!'
    unitest.deleteservice(server, service + ".MapServer", admin, password)
    print 'Start delete PostgreDB!'
    unitest.deleteDB(mxd)
    # print 'Start delete Directory!'
    # unitest.deleteDir(folder)
    print 'Start delete MongoDB!'
    unitest.deleteMongo(service)
    print 'All done'