#!/usr/bin/env bash
sudo rm /var/lib/apt/lists/lock
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python3.6
sudo apt install python3-pip
pip3 install --user pyqt5
sudo apt-get install python3-pyqt5
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
sudo apt-get install python3-pygraphviz
pip3 install -r requirements.txt