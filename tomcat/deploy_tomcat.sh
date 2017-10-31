#!/bin/bash

$USER = gvm

cd /home/$USER/shdkej/board
./mvnw clean package
cp target/gvm.war /home/$USER/docker/tomcat/gvm.war
docker stop tomcat
docker rm tomcat

cd /home/$USER/docker/tomcat/
docker build -t tomcat .
docker run -d -p 80:8080 --name tomcat tomcat
docker restart tomcat
