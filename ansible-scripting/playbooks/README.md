# Ansible Test Outline

Steps ansible script needs to take:

1. git clone https://github.com/ImogenWren/SBC_Testing ./remotelabs/SBC_Testing
2. cp ./remotelabs/sbc-testing/python-scripting/dataDump.py /home/odroid/dataDump.py
3. chmod +x dataDump.py
4. echo "@reboot sudo python3 /home/odroid/dataDump.py" | sudo crontab
5. sudo systemctl enable cron
6. nano genData.txt
7. sudo reboot
8. cat genData.txt | grep "all work and no play"  # Some method of automated testing that file has been written to?
