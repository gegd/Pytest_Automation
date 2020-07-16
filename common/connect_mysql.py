import pymysql
#
# dbinfo = {
#     'host': '49.235.92.12',
#     'user': 'root',
#     'password': '123456',
#     'port': 3309
# }


class DbConnect():
    def __init__(self, database=''):
        # self.db_conf = db_conf
        # 打开数据库连接
        self.db = pymysql.connect(
                                  host='10.0.34.104',
                                  user='ua_online_saas',
                                  password='0WhVmckXIn4qgPQ5S3',
                                  port=3306,
                                  database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  )
        # 使用cursor方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql_name):
        self.cursor.execute(sql_name)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql_name):
        try:
            # 执行sql语句
            self.cursor.execute(sql_name)
            # 提交修改
            self.db.commit()
        except:
            self.db.rollback()

    def close(self):
        self.db.close()


if __name__ == '__main__':
    db_connect = DbConnect(database='online_saas')
    sql_name = 'SELECT * FROM purchase_agreement WHERE tenant_id = "3701"'
    res = db_connect.select(sql_name)
    print(res)