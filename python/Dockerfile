FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y vim git curl python3 python3-pip  exuberant-ctags ack-grep fish
RUN pip3 install pytest pep8 flake8 pyflakes isort yapf

RUN curl -O https://raw.githubusercontent.com/fisadev/fisa-vim-config/master/config.vim
RUN ln config.vim ~/.vimrc

RUN pip3 install flask redis coverage pytest

WORKDIR /usr/src/app
