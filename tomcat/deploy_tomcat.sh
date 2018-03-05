#!/bin/bash

$USER = gvm

cd /home/$USER/shdkej/board
./mvnw clean package
cp target/gvm.war /home/$USER/docker/tomcat/gvm.war
docker stop docker_tomcat_1
docker rm docker_tomcat_1

cd /home/$USER/docker/tomcat/
#docker build -t tomcat .
#docker run -d -p 90:8080 --name tomcat tomcat
docker-compose up -d --build tomcat
docker restart docker_tomcat_1
