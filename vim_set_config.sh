#!/usr/bin/env bash
## by Chang Liu, this script is used for configuring the VIM using this repo
## Just first download this raw script then it will do everything well
cd ~
mkdir .tmp .undodir
touch .vim_mru_files
git clone git@github.com:deercoder/vimrc.git .vim
cp .vim/.sysrc_sample.vim ./.sysrc.vim
cp .vim/.vimrc_sample ./.vimrc
