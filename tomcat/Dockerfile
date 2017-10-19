FROM tomcat:9.0
#톰캣
MAINTAINER shdkej@gmail.com

RUN apt-get update -qq
RUN apt-get install -y -qq vim git
#COPY server.xml /usr/local/conf/server.xml
RUN sed -i '/autoDeploy="true">/a\<Context docBase="gvm" path="/" reloadable="true"/>' conf/server.xml

COPY gvm.war /gvm.war
RUN cp /gvm.war webapps/gvm.war
#RUN git clone https://github.com/shdkej/shdkej.git
#RUn cp shdkej/gvm.war webapps/gvm.war

ADD tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

# VOLUME /home/pi/docker/tomcat

EXPOSE 8080
