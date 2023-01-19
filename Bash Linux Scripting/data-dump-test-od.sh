
#!/bin/sh
# data-dump-test-od.sh
# Navigate to home directory, then to this directory.
# Then execute all commands nessissary to set up odroid for dataDump power cycle test
# NOTE: Modiffied for Odroid
# 1. add this file to home directory
# 2. chmod +x data-dump-test-setup.sh
# 3. sudo sh data-dump-test.sh
# 


cd /
echo Cloning sbc-testing repo...
git clone https://github.com/ImogenWren/SBC_Testing /home/odroid/remotelabs/sbc-testing
ls
sleep 2
echo copying python file
sleep 2
cp /home/odroid/remotelabs/sbc-testing/python-scripting/dataDumpPi.py /home/odroid/dataDump.py
cd /
sudo chmod +x /home/odroid/dataDump.py
sleep 2
echo Modifying Crontab
sleep 1
echo "@reboot sudo python3 /home/odroid/dataDump.py" | sudo crontab
sudo systemctl enable cron
sleep 2
date >> /home/odroid/genData.txt
cat genData.txt
sleep 5
echo Script Finished
#sudo reboot

