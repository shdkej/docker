FROM jasonrivers/nagios:latest

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y -qq python3 vim git
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python
RUN easy_install pip
RUN pip install twx.botapi
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN wget -O /usr/local/bin/nagios_telegram.py https://raw.githubusercontent.com/pommi/telegram_nagios/master/telegram_nagios.py
RUN chmod 755 /usr/local/bin/nagios_telegram.py

ADD etc/ /opt/nagios/etc/
# VOLUME /opt/nagios/etc/
EXPOSE 80
