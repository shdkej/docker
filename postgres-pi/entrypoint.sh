#!/bin/bash


service postgresql start
service apache2 start
su - postgres
mkdir /test
psql -f /PGSQL_all.dump postgres
