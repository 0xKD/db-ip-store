db-ip-store
===========

Store CSV from [dp-ip.com](https://db-ip.com/db/) to MySQL or SQLite for fast IP-based search.


## To make an SQLite db:

This is based on the IP -> city database.

Download [city-db](https://db-ip.com/db/download/city):

```bash
gunzip -c downloaded_file.gz > iplogs.csv
```

Filter out only IPv4 addresses into __ipv4log.csv__:

```bash
touch ipv4logs.csv
head -n `grep '224.0.0.0' iplogs.csv -n | cut -d':' -f1` iplogs.csv > ipv4logs.csv
```

Then run

```bash
$ python initsqlite.py
$ python savetosqlite.py
$ python iplookup.py '123.45.67.89'
```

----

