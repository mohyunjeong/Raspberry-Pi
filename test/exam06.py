import pymysql as ps

conn = ps.connect(host='localhost', user='root', passwd='1234', db='test')

curs = conn.cursor()
sql = 'select * from info'

curs.execute(sql)

result = curs.fetchall()

for n, a, t in result :
    print('(({}, {}, {}),)'.format(n, a, t))
