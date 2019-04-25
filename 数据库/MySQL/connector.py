import pymysql


# 连接MySQL数据库
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='682240',
                             db='practice',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# 创建sql语句，并执行
sql = 'INSERT INTO users (`id`, `userid`,`department_id`) VALUES' \
      ' (4,5,6)'
cursor.execute(sql)

# 提交SQL
connection.commit()