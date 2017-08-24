FROM tomcat:8.0

RUN apt-get update
RUN apt-get install git
RUN git clone https://github.com/shdkej/shdkej.git
RUN cp shdkej/gvm.war webapps/gvm.war

EXPOSE 8080
