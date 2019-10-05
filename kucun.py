import pymysql
import json


conf = json.load(open("conf.json"))  # 配置信息

def kucuninfo():
    print("请输入待插入的商品信息")
    uname = input("请输入商品名称:")
    jinjia = input("请输入商品进价:")
    shoujia = input("请输入商品售价:")
    rkl = input("请输入商品入库量:")

    
    # 连接数据库，conn为Connection对象
    conn = pymysql.connect(conf["db_server"], conf["db_user"], conf["db_password"], conf["db_name"])
    try:
        with conn.cursor() as cur:  # 获取一个游标对象(Cursor类)，用于执行SQL语句
            # 执行任意支持的SQL语句
            cur.execute("INSERT INTO commodity (uname,jinjia,shoujia,rkl) VALUES (%s,%s,%s,%s)", (uname,jinjia,shoujia,rkl))
            # 通过游标获取执行结果
            # rows = cur.fetchone()
            conn.commit()
    finally:
        # 关闭数据库连接
        conn.close()
