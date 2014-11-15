import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('iplocs.db')
    c = conn.cursor()
    c.execute('CREATE TABLE dbip_country(ip_start varbinary(16) PRIMARY KEY, ip_end varbinary(16), country char(2))')
    conn.commit()
    conn.close()

