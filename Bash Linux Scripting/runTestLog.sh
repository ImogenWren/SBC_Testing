
#!/bin/sh
# runTestLog.sh
# Navigate to home directory, then to this directory.
# Then execute python script
# Add This line to root crontab `sudo crontab -e` file
# @reboot sh runTestLog.sh


cd /
cd /home/odroid/remotelabs/
date >> TEST_LOG.log
sudo python3 testLog.py >> TEST_LOG.log


