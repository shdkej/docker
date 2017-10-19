#!/bin/bash
pg_dumpall > /etc/postgresql/9.5/main/data/PGSQL_all.dump
pg_dumpall > /etc/postgresql/9.5/main/data/PGSQL_$(date +"%Y%m%d%H%M%S").dump
find /etc/postgresql/9.5/main/data/ -type f -mtime +10 | sort | xargs rm -f

