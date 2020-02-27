import pymysql.cursors
s = "anhyeuem123."

def getConnection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=s,
        db='test',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
