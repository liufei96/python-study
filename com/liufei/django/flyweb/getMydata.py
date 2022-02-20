'''
getdata文件：文件名自己定义，主要方式处理数据库相关逻辑。
'''

import pymysql

def get_data():
    conn = pymysql.connect(
        host='192.168.220.130',
        port=3306,
        user='root',
        password='123456',
        database='test',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 获取所有数据
    cursor.execute("select * from userinfo;")
    data = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return data