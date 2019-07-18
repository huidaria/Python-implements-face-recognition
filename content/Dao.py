import pymysql
#根据id获取用户的信息
def getInfo(id):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',  #写自己的密码和账户
        passwd='root',
        db='db5', #写自己的数据名称
        charset='utf8'
    )
    # 使用cursor()方法创建一个游标对象
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

    # 使用execute()方法执行SQL语句
    sql = "SELECT * FROM staff where id= %s"
    value = id
    cursor.execute(sql, value)

    # 使用fetall()获取全部数据
    data = cursor.fetchone()

    # 打印获取到的数据
    # print(data)

    # 关闭游标和数据库的连接
    cursor.close()
    db.close()

