# import pymysql as ps
import databas as db

# conn = ps.connect(host='localhost', user='root', passwd='1234', db='test')

# curs = conn.cursor()

def select_db() :
    sql = 'select * from sensordb'
    result = db.db_select(sql)
    r = '<br>'.join(map(str, result))
    return r
    
# join, map


# curs.execute(sql)

# result = curs.fetchall()

# for s, t in result :
#     print('sensing : {} / ts : {}'.format(s, t))