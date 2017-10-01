FROM dordoka/rpi-tomcat
#라즈베리파이용 톰캣
MAINTAINER shdkej@gmail.com

RUN apt-get update
RUN apt-get install -y vim git
COPY server.xml /usr/local/conf/server.xml
# RUN sed -i '/autoDeploy="true">/a\<Context docBase="gvm" path="/" reloadable="true"/>" conf/server.xml
COPY /home/pi/shdkej/gvm.war /gvm.war
# RUN git clone https://github.com/shdkej/shdkej.git
RUN cp shdkej/gvm.war webapps/gvm.war

# VOLUME /home/pi/docker/tomcat

EXPOSE 8080
