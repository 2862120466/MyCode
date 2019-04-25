import pymysql

class MysqlSearch:
    def connect(self,db_name):
        try:
            self.conn = pymysql.connect(user='root',
                                   password='682240',
                                   host='localhost',
                                   port=3306,
                                   db=db_name,
                                   charset='utf8'
                                   )
            print('成功连接MySQL数据库:',db_name)
            # 创建游标,并选择参数cursor设置返回数据为字典对象
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except pymysql.Error as e:
            print('连接出错了：%s'%e)

    def close(self):
        try:
            if self.conn:
                self.cursor.close()
                self.conn.close()
                print('成功断开连接')
            else:
                print('当前没有连接到数据库')
        except pymysql.Error as e:
            print('连接出错了：%s' % e)

    def select_table(self, offset, page_size):
        sql_select = 'select * from beauty limit %s,%s'
        self.cursor.execute(sql_select,( offset, page_size ))

        data = self.cursor.fetchall()
        keys = list( data[0].keys() )
        print( keys,'\n' )

        for i in data:
            print( list(i.values()) )



def main():
    db_name = input('请输入你想要连接的数据库名：').strip(' ')
    db = MysqlSearch()
    db.connect(db_name)
    db.select_table(2,3)
    db.close()

if __name__ == '__main__':
    main()