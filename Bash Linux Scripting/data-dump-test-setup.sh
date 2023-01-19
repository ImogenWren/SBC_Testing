
#!/bin/sh
# data-dump-test-setup.sh
# Navigate to home directory, then to this directory.
# Then execute all commands nessissary to set up odroid for dataDump power cycle test
# NOTE: Modify scriopts for rpi for testing
# 1. add this file to home directory
# 2. chmod +x data-dump-test-setup.sh
# 3. sudo sh data-dump-test.sh
# 


cd /
echo Cloning sbc-testing repo...
git clone https://github.com/ImogenWren/SBC_Testing ./remotelabs/SBC_Testing
echo copying python file
cp ./remotelabs/sbc-testing/python-scripting/dataDump.py /home/odroid/dataDump.py
chmod +x dataDump.py
echo Modifying Crontab
echo "@reboot sudo python3 /home/imogen/dataDump.py" | sudo crontab
sudo systemctl enable cron
echo date >> genData.txt
sudo reboot


