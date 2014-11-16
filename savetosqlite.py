import socket
import csv
import sqlite3

if __name__ == '__main__':

    conn = sqlite3.connect('iplocs_city.db')
    r = conn.cursor()

    with open('ipv4log_city.csv', 'r') as csvlog:
        lines = csv.reader(csvlog, delimiter=',', quotechar='"')
        for vals in lines:
            r.execute('INSERT into dbip_city VALUES(?, ?, ?, ?, ?)',
                    [sqlite3.Binary(socket.inet_aton(vals[0])),
                        sqlite3.Binary(socket.inet_aton(vals[1])),
			vals[2],
			unicode(vals[3], 'utf-8'),
			unicode(vals[4], 'utf-8')])
        conn.commit()

