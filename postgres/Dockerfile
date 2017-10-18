FROM ubuntu

RUN apt-get -y update
RUN apt-get install -y -qq postgresql apache2 phppgadmin vim

WORKDIR /etc/postgresql/9.5/main
RUN sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" postgresql.conf
RUN echo "host all all 0.0.0.0/0 password" >> pg_hba.conf
RUN sed -i "s/Require local/Require all granted\nAllow from all/g" /etc/apache2/conf-enabled/phppgadmin.conf
RUN sed -i "s/$conf['owned_only'] = false/$conf['owned_only] = true/g" /etc/phppgadmin/config.inc.php 

USER postgres
RUN (crontab -l 2>/dev/null; echo "*/5 * * * * /postgres_backup.sh") | crontab -
RUN mkdir /etc/postgresql/9.5/main/data

EXPOSE 5432
EXPOSE 80


ENV PGDATA = /etc/postgresql/9.5/main
ENV POSTGRES_DB gvm
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 123456
ENV POSTGRES_INITDB_ARGS=--encoding=UTF-8

#CMD service postgresql start && service apache2 start && /bin/bash

VOLUME ["/etc/postgresql/9.5/main"]
ADD PGSQL_all.dump /PGSQL_all.dump
ADD postgres_backup.sh /postgres_backup.sh
#ADD entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT /entrypoint.sh

USER postgres
RUN service postgresql start && psql -f /PGSQL_all.dump
USER root
CMD service postgresql start && service apache2 start && /bin/bash
