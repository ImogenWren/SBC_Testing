# Automated Testing


The ideal scenario is an additional SBC to act as the test coordinator. This can run the testPing.py (or similar) script and send and email if an offline host is detected.

- If Test Coordinator is powered from the same power supply it should only run script when all hosts should also be alive
- Emailing is the ideal situation, however requires internet access, so as a workaround it will simply log to file each host that is down and for how long 
  - Goal 1: Log Host down time during every test then manually calculate down time
  
  
  
## Outline

- Crontab task to call sh script `runTestLog.sh` on reboot.
```
#!/bin/sh
# runTestLog.sh
# Navigate to home directory, then to this directory.
# Then execute python script
# Add This line to root crontab `sudo crontab -e` file
# @reboot sh runTestLog.sh
```
- runTestLog.sh calls up python script `testLog.py` main output is redirected to test_log.log
- Python script will also log only OFFLINE hosts to offline_log.log
	- Script will log ip, host and times of non responsive hosts.
	- NOTE: odroid 6 and 10 will sometimes be off, but should reset with the rest of the SBCs



Problem 1:
- Running Crontab on bootup - This is solveable I have before just need to work out how I have done kiosks in past.

Problem 2:
- No Switched power left so test coordinator is always powered.
- SOLUTION: Voltage sense pin to one of the other switched SBCs. This will be 5v so will need a voltage dividor to drop down to 3.3v to be read by the TC SBC.
- Use Values 10k and 5.6k for 3.2 logic high
  
