# ODroid Power Cycle Testing Procedure
_The following document outlines the procedure & rational for power cycle testing of ODroid SBCs._


## Purpose of Testing
 - Ascertain the root cause of memory corruption during power cycles & normal use of ODroid SBCs.
 - Establish the difference between SD cards and EMMC boot drive options.
 - Establish difference between hard shut down (Power removed suddenly) and Sheduled shutdown.
 - Compare performance when SBC is powered via 12v input or regulated 5v direct to the 5v rail.
 - Aim to complete approximately 200 hard shutdown power cycles.
 

## Timeframe
In order to complete between 192 and 240 hard shutdowns, with one power on/power off cycle taking 30 minutes to complete, 
the test should be run for between 96 and 120 total hours, with a check once daily for failed units.
This is anticipated to take one single work week, with the test starting on Monday morning, close to 0900 hours,
and finishing before lunchtime on Friday, to enable data to be recorded as soon as the test is finished.
 

## Test Articles
_The following configurations will be tested under the same conditions, preferably concurrently_

| SBC 			| Memory/Storage    	|Power Supply		| Quantity 	| Power Cycle	| 
|---			|---			|---			|---		|---		|
|ODroid 		| SD Card		| 12v DC to Vin jack(2A)|   x2		| 	Yes	|
|ODroid 		| EMMC			| 12v DC to Vin jack(2A)|   x2		| 	Yes	|
|ODroid 		| SD Card		| 5v Rail (500mA Max!)	|   x2		| 	Yes	|
|ODroid 		| EMMC			| 5v Rail (500mA Max!)	|   x2		| 	Yes	|
|Raspberry Pi	| SD Card			| USB Power Supply		|x1		|Yes - Control 0	|
|ODroid			| EMMC			| 5v Rail (500mA Max!)	|x1	|No - Control 1	|
|ODroid			| EMMC (Dont have enough to run concurrently - SD card for now|        		|x1	|SOFT SHUTDOWN - Cron Task to perform safe shutdown. Reboots with power strip - Control 2 |

- Each SBC will have been set up from a known configuration, I.E. a formatted storage medium flashed with the lastest stable OS version.
- Each SBC will be running a cronjob to log the current time to a file every 3 minutes saved at `./remotelabs/SCB_TEST.log`
- SBCs that are being used with SOFT reset will have an additional cronjob to shut down every 10 minutes. This means they will cycle on for 10 mins, shutdown,
then be rebooted by a power cycle that happens with the rest of the SBCs, ensuring that the same number of power down cycles are performed.

## Test Setup
- All SBCs given a unique and incremented IP Address (192.168.1.X) and a logical hostname mirroring the IP
	- https://www.cyberciti.biz/faq/ubuntu-change-hostname-command/ 
		- Type the following command to edit /etc/hostname using nano or vi text editor: 
			`sudo nano /etc/hostname`
		- Delete the old name and setup new name.
		- Next Edit the /etc/hosts file
			`sudo nano /etc/hosts`
		- Reboot the system to changes take effect: `sudo reboot`.
	- https://ubuntu.com/server/docs/network-configuration	
- All SBCs are plugged into a LAN via network switches
- Enable SSH On all SBCs
- Ensure connection to wifi to set date and time correctly. NOTE: Issue with interfacing with university internet, could use additional Rpi as router but scope is too large. Log times might just be wrong, or set time & date manually https://www.cyberciti.biz/faq/howto-set-date-time-from-linux-command-prompt/
- `date --set="STRING"`
- `sudo date --set="2 OCT 2006 18:00:00`
- Ensure Cronjobs set up as below

- Engineering Laptop set to static ip `192.168.1.100`

## Cronjob
To Edit Cronjob file: 
`crontab -u imogen -e` <br>

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

- Power Strip is turned on and test is run for between ___ and ___ hours.
- Daily check for communication from each SBC using PING over LAN.
- Note down any SBCs that do not respond to pings, and last known time of operation. (Could be automated in future?)
- Attempt SSH into any "failed" SBCs to confirm status. Note down any performance issues or inactivity.
- If 

### End of Test

- After a maximum of ___ hours, each SBC can be soft shut down, the power strip is turned off and SBCs are unplugged from power sources.

### Data Gathering

- Each SBC is powered individually and checked for memory corruption.
	- Copy log from `./remotelabs/SCB_TEST.log` for later analysis
	
 Record results and evaluate options to reduce risk of memory corruption in deployed systems.
 SBC Table

| SBC Type | User | Hostname | Memory | Power | IP |
|---		|---	|---	|---	|---	|---	|
| Raspberry Pi	| imogen |pi01  | SD Card | Rpi PSU | 192.168.1.1 |
| oDroid	| odroid|odroid02 | emmc| 12v	| 192.168.1.2|
|oDroid		| odroid| odroid03| EMMC | 12v  |192.168.1.3|



# Notes
https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804



