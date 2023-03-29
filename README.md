# ODroid Power Cycle Testing Procedure
_The following document outlines the procedure & rational for power cycle testing of ODroid SBCs._


## Purpose of Testing
 - Ascertain the root cause of memory corruption during power cycles & normal use of ODroid SBCs.
 - Establish the difference between SD cards and EMMC boot drive options.
 - Establish difference between hard shut down (Power removed suddenly) and Sheduled shutdown.
 - Compare performance when SBC is powered via 12v input or regulated 5v direct to the 5v rail.
 - 2nd round of testing aims to push read/write cycles on external memory devices to discover limits of operation

 

## Timeframe
- Test is to be run indefinatly or until failure is seen.
 

## Test Articles
_The following configurations will be tested under the same conditions, preferably concurrently_

| SBC 			| Memory/Storage    	|Power Supply		| Quantity 	| Power Cycle	| 
|---			|---			|---			|---		|---		|
|ODroid 		| SD Card		| 12v DC to Vin jack(2A)|   x2		| 	Yes	|
|ODroid 		| EMMC			| 12v DC to Vin jack(2A)|   x2		| 	Yes	|
|ODroid 		| SD Card		| 5v Rail (500mA Max!)	|   x2		| 	Yes	|
|ODroid 		| EMMC			| 5v Rail (500mA Max!)	|   x2		| 	Yes	|
|Raspberry Pi	| SD Card			| USB Power Supply	|x1		|Yes - Control 0	|
|ODroid			| EMMC			| 5v Rail (500mA Max!)	|x1		|No - Control 1	|
|ODroid			| EMMC (Dont have enough to run concurrently - SD card for now|        	|x1	|SOFT SHUTDOWN - Cron Task to perform safe shutdown. Reboots with power strip - Control 2 |

- Each SBC will have been set up from a known configuration, I.E. a formatted storage medium flashed with the lastest stable OS version.



## Test Setup
- All SBCs given a unique and incremented IP Address (192.168.1.X) and a logical hostname mirroring the IP
- All SBCs are plugged into a LAN via network switches
- Enable SSH On all SBCs
- Ensure data-dump-test Cronjobs set up as below.
- All Files and Scripts used to setup, run and gather data for tests found in data-dump-test directory.

Step 1: Copy files across using script from linux machine
Step 2: Log into remote machine and run script to install crontab
step 3: make sure crontab runs test log python script on test supervisor
step 4: cat testLog.log and look for non-responsive clients

## Data Dump Test

- Cronjob calls a python script
	- Python Script
		- continuously writes data to external memory device.
		- Copies file to a different location.
		- deletes both copies of the file.
		- repeats
		



## Cronjob
-- NEW


-- Old
To Edit Cronjob file: 
`crontab -u odroid -e` <br>

_First cronjob is installed on each SBC to log data and time periodically_
```
*/3 * * * * date >> ./remotelabs/SBC_TEST.log
```
_Second cronjob is installed on control 2, to soft shutdown SBC before power is removed_
```
*/10 * * * * sudo shutdown
```
_Alternative 2nd cronjob to also save shutdown notice to the log_ **Tested & Working**
```
*/10 * * * * { echo "Shutdown Inititated @"; date; } | tr "\n" " "  >> ./remotelabs/SBC_TEST.log; sudo shutdown
```

Ensure Cronjobs are active:
`sudo systemctl enable cron` <br>
Check Cronjobs:
`crontab -l` <br>

Ensure that folder exists for log file - crontab will not work if folder does not exist.
`mkdir remotelabs` 

NOTE: Issue with shutdown command on odroid. Because of course there is https://forum.odroid.com/viewtopic.php?t=34015 - could be a sudoers issue
https://askubuntu.com/questions/173924/how-to-run-a-cron-job-using-the-sudo-command - going the quick and dirty route of piping the password to the cronjob.
If expanding on methodology, or connecting SBCs to WAN then use safer option of shutdown as root crontask. - NOTE does not work. going with installing cronjob as root
`sudo crontab -e` (NOTE! crongjob still needs sudo infront of shutdown to work!)

## Test Procedure

### Before starting
- Each SBC is checked for basic operation and set up:
	- Power SBC with suitable power supply. (12v 2A for Odroid, 5v Rpi Power Supply for Rpi)	 
 	- Set Static IP, hostname and login details
	- Login Details & IP labeled onto SBC
	- Install/test function of cronjob tasks
	- Shutdown and move to test rig

- Power up all SBCs and test LAN by pinging each SBC. (See testPing.py script)
	- Note any SBCs that do not reply
- SSH into and soft shutdown each SBC
- 


- Each SBC (Except control) is plugged into an unpowered power strip.

- Power strip is plugged into a wall socket, via 24h mechanical timer plug, set to change state at every 15 minute interval.

### Running Test

- Power Strip is turned on and test is run indefinatly
- Online status is checked by an additional SBC running test-log.py script and outputting a log of power outages and ping responses to testLog.log in user folder

### End of Test

.

### Data Gathering

- Each SBC is powered individually and checked for memory corruption.
	- Copy log from `./remotelabs/SCB_TEST.log` for later analysis
	
 Record results and evaluate options to reduce risk of memory corruption in deployed systems.
 
 # SBC Table

| SBC Type 	| User 		| Hostname 	| Memory 	| Power 	| IP 		|
|---		|---		|---		|---		|---		|---		|
| Raspberry Pi	| imogen 	| pi01  	| SD Card 	| Rpi PSU 	| 192.168.1.1 	|
| oDroid	| odroid	| odroid02 	| EMMC		| 12v		| 192.168.1.2	|
| oDroid	| odroid	| odroid03	| EMMC		| 12v 		| 192.168.1.3	|
| oDroid	| odroid	| odroid04	| EMMC		| 5v		| 192.168.1.4	|
| oDroid	| odroid	| odroid05	| EMMC		| 5v - No Shutdown| 192.168.1.5	|
| oDroid	| odroid	| odroid06	| EMMC		| 12v - Soft Shutdown| 192.168.1.6|
| oDroid	| odroid	| odroid07	| SD Card	| 12v 		| 192.168.1.7	|
| oDroid	| odroid	| odroid08	| SD Card	| 12v 		| 192.168.1.8	|
| oDroid	| odroid	| odroid09	| SD Card	| 5v 		| 192.168.1.9	|
| oDroid	| odroid	| odroid10	| SD Card	| 5v  - Soft Shutdown	| 192.168.1.10	|
| oDroid	| odroid	| odroid11	| SD Card	| 12v - No Shutdown	| 192.168.1.11	|


# Notes
https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804



