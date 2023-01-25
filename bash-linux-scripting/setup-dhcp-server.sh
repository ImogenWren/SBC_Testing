
#!/bin/sh
# setup-dhcp-server.sh
# Navigate to home directory, then to this directory.
# Then execute all commands nessissary to set up raspberry pi as DHCP server
# PREREQS:
# Raspberry Pi should be setup with Static IP Address
# TO RUN:
# 1. add this file to home directory
# 2. chmod +x setup-dhcp-server.sh
# 3. sudo sh setup-dhcp-server.sh


cd /
echo Starting DHCP Server Setup
#git clone https://github.com/ImogenWren/SBC_Testing /home/imogen/remotelabs/sbc-testing
mkdir /home/imogen/dhcp-server
touch /home/imogen/dhcp-server/static-config
STATIC_IP=$(ifconfig | grep -o -P '.192.168.1.{0,4}' | grep -v 255 )
echo $STATIC_IP
echo -e "interface eth0 \nstatic ip_address=${STATIC_IP}/24" >> /home/imogen/dhcp-server/static-config
echo -e "static routers=192.168.1.0 \nstatic domain_name_servers=192.168.1.0 8.8.8.8" >> /home/imogen/dhcp-server/static-config
echo "\n\n"
cat /home/imogen/dhcp-server/static-config
echo "\n\n"
ls
sleep 10
echo Installing DNSMasq
sudo apt install dnsmasq
echo "interface=eth0 \nbind-dynamic \ndomain-needed \nbogus-priv \n	dhcp-range=192.168.1.30,192.168.1.90,255.255.255.0,24h" >> /etc/dnsmasq.conf
sudo service dnsmasq restart
echo DHCP Sever Setup Complete. Please Reboot now to apply settings!