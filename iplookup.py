import socket
import sys
import sqlite3

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: $ python iplookup.py "1.32.34.109"'
    else:
        _ip = sys.argv[1]
        conn = sqlite3.connect('iplocs_city.db')
        r = conn.cursor()
        r.execute('SELECT country FROM dbip_country WHERE ip_start <= ? order by ip_start desc limit 1',
                [sqlite3.Binary(socket.inet_aton(_ip))])
        for row in r.fetchall():
            print row

