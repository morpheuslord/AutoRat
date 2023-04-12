#!/bin/bash

RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
ENDCOLOR="\e[0m"

echo -e "${YELLOW}==============================================${ENDCOLOR}"
echo -e "              ${RED} Installing Packages ${ENDCOLOR}"
echo -e "${YELLOW}==============================================${ENDCOLOR}"

apt-get update && apt-get upgrade
apt-get install -y python3 python3-pip git curl wget build-essential git ruby bundler ruby-dev bison flex autoconf automake zipalign apache2

echo -e "${YELLOW}==============================================${ENDCOLOR}"
echo -e "             ${RED} Installing Metasploit ${ENDCOLOR}"
echo -e "${YELLOW}==============================================${ENDCOLOR}"
chmod 777 msfinstall
sudo bash msfinstall

echo -e "${YELLOW}==============================================${ENDCOLOR}"
echo -e "            ${RED} Setting Apache2 service ${ENDCOLOR}"
echo -e "${YELLOW}==============================================${ENDCOLOR}"
mkdir /var/www/apk
cp apk.conf /etc/apache2/sites-available/
cd /etc/apache2/sites-available/
a2ensite apk.conf
service apache2 reload

echo -e "${YELLOW}==============================================${ENDCOLOR}"
echo -e "            ${RED} Installation Complete ${ENDCOLOR}"
echo -e "${YELLOW}==============================================${ENDCOLOR}"