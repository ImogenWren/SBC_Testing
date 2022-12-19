# ODroid Power Cycle Testing Procedure
_The following document outlines the procedure & rational for power cycle testing of ODroid SBCs._


## Purpose of Testing
 - Ascertain the root cause of memory corruption during power cycles & normal use of ODroid SBCs.
 - Establish the difference between SD cards and EMMC boot drive options.
 - Compare performance when SBC is powered via 12v input or regulated 5v direct to the 5v rail.
 - Aim to complete between ___ and ___ number of hard shutdown power cycles.
 

## Timeframe
In order to complete between ___ and ___ hard shutdowns, with one power on/power off cycle taking 30 minutes to complete, 
the test should be run for between ___ and ___ hours.
 

## Test Articles
_The following configurations will be tested under the same conditions, preferably concurrently_

| SBC 			| Memory/Storage    |Power Supply		| Quantity 	| Power Cycle	|
|---			|---				|---				|---		|---			|
|ODroid 		| SD Card			| 12v DC to Vin jack|   x2		| 	Yes			|
|ODroid 		| EMMC				| 12v DC to Vin jack|   x2		| 	Yes			|
|ODroid 		| SD Card			| 5v Rail			|   x2		| 	Yes			|
|ODroid 		| EMMC				| 5v Rail			|   x2		| 	Yes			|
|Raspberry Pi	| SD Card			| USB Power			|	x1		|	Yes			|
|ODroid			| EMMC				| 5v Rail?			|	x1		|	No - Control (Any way to check that it has remained powered for duration, in case of external power outages?)|
|ODroid			| 					|        			|	x1		|	No - Cron Task to perform safe shutdown & Reboot as a control?    |

Each SBC will have been set up from a known configuration, I.E. a formatted storage medium flashed with the lastest stable OS version, with the relevent Remote Labs
files downloaded from GitHub. ? This will include a script/cronjob to log the current time to a file saved at ../../../../PowerCycleLog.txt ? 

## Test Procedure

### Before starting
- Each SBC is checked for basic operation 
	- TODO# Do we have a way of quantifying this?
	
- Each SBC is plugged into an unpowered power strip.

- Power strip is plugged into a wall socket, via 24h mechanical timer plug, set to change state at every 15 minute interval.

### Running Test

- Power Strip is turned on and test is run for between ___ and ___ hours.

### End of Test

- After a maximum of ___ hours, the power strip is turned off and SBCs are unplugged from power sources.

### Data Gathering

- Each SBC is powered individually and checked for memory corruption.
	- TODO# How do we quantify this, does a memory corruption tend to cause SBC to be unable to boot?
	
- Record results and evaluate options to reduce risk of memory corruption in deployed systems.





# Notes
https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804



