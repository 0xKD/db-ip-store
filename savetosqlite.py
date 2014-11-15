import socket
import csv
import sqlite3

if __name__ == '__main__':

    conn = sqlite3.connect('iplocs.db')
    r = conn.cursor()

    with open('ipv4log.csv', 'r') as csvlog:
        lines = csv.reader(csvlog, delimiter=',', quotechar='"')
        for vals in lines:
            r.execute('INSERT into dbip_country VALUES(?, ?, ?)',
                    [sqlite3.Binary(socket.inet_aton(vals[0])),
                        sqlite3.Binary(socket.inet_aton(vals[1])),
                        vals[2]])
        conn.commit()

