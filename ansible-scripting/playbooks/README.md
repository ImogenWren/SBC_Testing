# Ansible Test Outline

Steps ansible script needs to take:

1. git clone https://github.com/ImogenWren/SBC_Testing ./remotelabs/SBC_Testing
2. cp "./rmotelabs/sbc-testing/python-scripting/dataDump.py /home/odroid/dataDump.py
3. echo @reboot sudo python3 /home/odroid/dataDump.py >> sudo crontab -e
4. nano genData.txt
5. sudo reboot
6. cat genData.txt | grep "all work and no play"  // Some method of automated testing that file has been written to?
