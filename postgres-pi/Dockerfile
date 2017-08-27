FROM resin/rpi-raspbian:jessie

RUN apt-get update
RUN apt-get install -y postgresql

WORKDIR /etc/postgresql/9.4/main
RUN sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" postgresql.conf
RUN echo "host all all 0.0.0.0/0 password" >> pg_hba.conf

EXPOSE 5432
ENV POSTGRES_DB gvm
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 123456
ENV POSTGRES_INITDB_ARGS=--encoding=UTF-8

#VOLUME ["/var/lib/postgresql"]


ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
