#!/bin/bash
pg_dumpall > /etc/postgresql/9.5/main/PG_all.dump
pg_dumpall > /etc/postgresql/9.5/main/PG_'date + %Y%m%d%H%M%S'.dump
find /etc/postgresql/9.5/main/ -type f -mtime +10 | sort | xargs rm -f

