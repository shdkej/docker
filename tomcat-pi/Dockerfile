FROM dordoka/rpi-tomcat
#라즈베리파이용 톰캣
MAINTAINER shdkej@gmail.com

#RUN apt-get update -qq
#RUN apt-get install -y -qq vim git
#COPY server.xml /usr/local/conf/server.xml
RUN sed -i '/autoDeploy="true">/a\<Context docBase="gvm" path="/" reloadable="true"/>' conf/server.xml
COPY gvm.war /gvm.war
# RUN git clone https://github.com/shdkej/shdkej.git
RUN cp /gvm.war webapps/gvm.war

# VOLUME /home/pi/docker/tomcat

EXPOSE 8080
