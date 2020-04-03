FROM golang:1.13
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y curl vim fish vim-gtk
RUN git clone https://github.com/shdkej/environment ~/environment
RUN sh ~/environment/minimal.sh
