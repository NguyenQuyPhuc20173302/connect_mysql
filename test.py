import connection

try:
    con = connection.getConnection()
    print('connect successful')
except:
    print('connect fail')
