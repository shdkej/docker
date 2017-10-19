#!/bin/bash

docker cp postgres:/etc/postgresql/9.5/main/data/PGSQL_all.dump /home/gvm/docker/postgres/PGSQL_all.dump
docker cp postgres:/etc/postgresql/9.5/main/data /home/gvm/docker/postgres/
