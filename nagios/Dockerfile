FROM jasonrivers/nagios:latest

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y -qq python3 vim git
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python
RUN easy_install pip
RUN pip install twx.botapi
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN wget -O /usr/local/bin/nagios_telegram.py https://raw.githubusercontent.com/pommi/telegram_nagios/master/telegram_nagios.py
RUN chmod 755 /usr/local/bin/nagios_telegram.py

COPY ./check_tomcat.pl /opt/nagios/libexec/check_tomcat.pl
COPY ./check_tomcat.py /opt/nagios/libexec/check_tomcat.py
COPY ./check_postgres /opt/nagios/libexec/check_postgres

WORKDIR /opt/nagios/libexec
RUN chmod 755 check_tomcat.pl && chmod 755 check_tomcat.py
WORKDIR /opt/nagios/libexec/check_postgres
RUN apt-get install -y libxml-xpath-perl
#RUN perl Makefile.PL
#RUN make
#RUN env -i make test
#RUN make install
RUN apt-get update && apt-get install -y postgresql

VOLUME /opt/nagios/etc/
EXPOSE 80
WORKDIR /opt/nagios/
