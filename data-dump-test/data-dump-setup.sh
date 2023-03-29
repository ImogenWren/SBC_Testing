
#!/bin/sh
# data-dump-test-od.sh
# Navigate to home directory, then to this directory.
# Then execute all commands nessissary to set up odroid for dataDump power cycle test
# NOTE: Modiffied for Odroid & all files are copied offline
# 1. add this file to home directory
# 2. chmod +x data-dump-test-setup.sh
# 3. sudo sh data-dump-test.sh
# 


cd /
ls
sleep 2
echo Changing File Permissions
sleep 2
cd /
sudo chmod +x /home/odroid/dataDump.py
sleep 2
echo Modifying Crontab
sleep 1
echo "@reboot sudo python3 /home/odroid/dataDump.py" | sudo crontab
sudo systemctl enable cron
sleep 2
date >> /home/odroid/genData.txt
cat /home/odroid/genData.txt
sleep 2
echo Script Finished
echo REBOOTING NOW
sudo reboot

