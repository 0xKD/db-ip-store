import socket
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: $ python iplookup.py "1.32.34.109"'
    else:
        _ip = sys.argv[1]
        conn = MySQLdb.connect(host='localhost',db='ipdb',user='root',passwd='root')
        r = conn.cursor()
        r.execute('SELECT country FROM dbip_country WHERE ip_start <= %s order by ip_start desc limit 1',
                (socket.inet_aton(_ip),))
        for row in r.fetchall():
            print row

