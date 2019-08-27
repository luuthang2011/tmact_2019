from pymongo import MongoClient


if __name__ == '__main__':
        client = MongoClient('mongodb://fimo:fimo!54321@10.101.3.204:27017/ks')
        db = client['ks']

        url = 'thiendiahoi'
        ms_table = 'Tbl_fc_magma'
        de_an = 'du_an_1'

        post = {
                    "url": url,
                    "ms_table": ms_table,
                    "de_an": de_an,
                    "visible": 0,
                    "opacity": 0.7
                }

        posts = db.map_services
        post_id = posts.insert_one(post).inserted_id
        print post_id