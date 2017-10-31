FROM ubuntu

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install wget build-essential apache2 php apache2-mod-php7.0 php-gd libgd-dev unzip
WORKDIR /tmp
RUN wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-4.2.0.tar.gz
RUN wget http://nagios-plugins.org/download/nagios-plugins-2.1.2.tar.gz
RUN userdd nagios && grouadd nagcmd && usermod -aG nagcmd nagios
RUN usermod -aG nagios,nagcmd www-data
RUN tar zxvf nagios-4.2.0.tar.gz
RUN tar zxvf nagios-plugins-2.1.2.tar.gz
WORKDIR nagios-4.2.0
RUN ./configure --with-command-group=nagcmd --with-mail=/usr/bin/sendmail --with-httpd-conf=/etc/apache2/
RUN make all
RUN make install && make install-init && make install-config && make install-commandmode && make install-webconf
RUN cp -R contrib/eventhandlers/ /usr/local/nagios/libexec/
RUN chown -R nagios.nagios /usr/local/nagios/libexec/eventhandlers
RUN /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
RUN sudo a2ensite nagios && sudo a2enmod rewrite cgi
RUN sudo cp /etc/init.d/skeleton /etc/init.d/nagios

#add env htpasswd plugin install service setup
