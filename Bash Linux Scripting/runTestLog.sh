
#!/bin/sh
# runTestLog.sh
# Navigate to home directory, then to this directory.
# Then execute python script
# Add This line to root crontab `sudo crontab -e` file
# @reboot sh runTestLog.sh


cd /
cd /home/odroid/remotelabs/
echo Starting Test Log
echo date
date >> TEST_LOG.log
#python3 testLog.py >> TEST_LOG.log # Logging could be done in python, but if running as background task anyway, there is nothing to print to CLI
python3 testLog.py


