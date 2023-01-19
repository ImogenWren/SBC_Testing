
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
git clone https://github.com/ImogenWren/SBC_Testing /remotelabs/sbc-testing
ls
sleep 2
echo copying python file
sleep 2
cp ./remotelabs/sbc-testing/python-scripting/dataDump.py /home/imogen/dataDump.py
cd /
sudo chmod +x dataDump.py
sleep 2
echo Modifying Crontab
sleep 1
echo "@reboot sudo python3 /home/imogen/dataDump.py" | sudo crontab
sudo systemctl enable cron
sleep 2
date >> /home/imogen/genData.txt
cat genData.txt
sleep 5
echo Script Finished
#sudo reboot


