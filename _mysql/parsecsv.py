import socket
import csv
import MySQLdb

if __name__ == '__main__':

    conn = MySQLdb.connect(host='localhost',db='ipdb',user='root',passwd='root')
    r = conn.cursor()

    with open('ipv4log.csv', 'r') as csvlog:
        lines = csv.reader(csvlog, delimiter=',', quotechar='"')
        for vals in lines:
            # print 'IP_START<{0}>_END<{1}>_COUNTRY<{2}>'.format(*vals)
            r.execute('INSERT into dbip_country VALUES(%s, %s, %s)',
                    (socket.inet_aton(vals[0]),
                        socket.inet_aton(vals[1]),
                        vals[2]))
        conn.commit()

