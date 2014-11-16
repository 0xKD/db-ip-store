import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('iplocs_city.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE dbip_city(
                ip_start varbinary(16) PRIMARY KEY,
                ip_end varbinary(16),
                country char(2),
                state varchar(80),
                city varchar(80)
                )
        ''')
    conn.commit()
    conn.close()
