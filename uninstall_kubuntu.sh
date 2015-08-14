#!/usr/bin/env bash
sudo aptitude remove kde-desktop
sudo apt-get purge kubuntu-desktop
sudo apt-get auto-remove
sudo apt-get install ubuntu-desktop
