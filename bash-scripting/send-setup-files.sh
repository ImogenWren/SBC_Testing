
#!/bin/sh
# send-setup-files.sh
# send all files for data dump test - the python file and the bash install script
# NOTE: Modiffied for Odroid
# 1. Run this file from its folder on local machine, example command:
# sh send-setup-files.sh user@host:destination/
# 2. go to remote host and run data-dump-install.sh



echo Copying Python File from Local To Host...
scp /home/imogen/remotelabs/sbc-testing/python-scripting/dataDump.py $1
sleep 2
echo copying setup script file
sleep 2
scp /home/imogen/remotelabs/sbc-testing/bash-linux-scripting/data-dump-setup.sh $1
sleep 2
echo copying genData.txt file
scp /home/imogen/remotelabs/sbc-testing/python-scripting/genData.txt $1
echo Script Finished
#sudo reboot

