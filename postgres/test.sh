#!/bin/bash
psql -h myhost -d mydb -U myuser < create.sql
pg_dump db1 > us-counties
pg_dump db2 > us-counties
pg_dump db3 > us-counties
pg_dump db4 > us-counties
pg_dump db5 > us-counties
pg_dump db6 > us-counties
pg_dump db7 > us-counties
pg_dump db8 > us-counties

psql -h myhost -d mydb -U myuser < test.sql
