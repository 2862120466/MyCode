import pymysql   #导入pymysql模块，这里面模块名称可以小写

try:
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='682240',
                         db='practice',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    you = db.cursor()  # 用cursor方法获取一个操作游标you
    you.execute('select * from beauty')  # 用execute方法执行查询mysql数据库所有信息的命令
    data = you.fetchall()  # 获取结果集中剩下的所有行

    for i in data:
        print(i)

    you.close()
    db.close()

except pymysql.Error as e:
    print('Error: %s'%e)


