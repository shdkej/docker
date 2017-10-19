FROM ubuntu
MAINTAINER shdkej

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y -qq python3 libreadline-dev libconfig-dev libssl-dev lua5.2 liblua5.2-dev libevent-dev libjansson-dev make git-core git vim python-setuptools
RUN git clone --recursive https://github.com/vysheng/tg.git
WORKDIR /tg
RUN ./configure
RUN make
RUN mkdir /tg/bot
WORKDIR /tg/bot
RUN git clone https://github.com/eternnoir/pyTelegramBotAPI.git
WORKDIR pyTelegramBotAPI
RUN python setup.py install


ADD /data/connect.py /tg/bot/connect.py
