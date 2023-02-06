# Test Log

Note results and observations down during testing.


Pre Test:

- odroid08 was not able to maintain network connection. Swapped out SBC but kept the same SD card - observing for any change.
  - No change with SBC Swapped. Suggest re-flashing SD card
  - 


## Test Log Day 1

- Test Started at 09:57   09/01/23
- All Hosts active:
- Host 8 still looking unreliable so will be replaced ASAP 
- odroid08 replaced at 10:31 09/01/23 - New one seems to be more reliable
- 

## Test Log Day 4

- No performance issues seen so far. 
	- Considering extending the test indefinatly untill failure
	- Increase frequency of crontab writing file to memory
	- Increase complexity of writing task, EG, move large files from point A to point B?
		- Python script to:
			- open/create a file
			- write a huge chunk of data to it.
			- Save the file
			- Delete the file
			- loop
			
## Test Log - End of Test
- No Failures seen so far.
- Installing python script to open/write/close file up to 300MB, delete file and start again on every SBC
- cal
	- dataDump.py
	- Installing Instructions:

- Copy dataDump.py to home directory 
- `sudo chmod +x dataDump.py`
- `crontab -e` -> `@reboot sudo python3 dataDump.py`
- `nano genData.txt`              # Not Nessissary
- `sudo chmod 777 genData.txt`    # Might not be nessissary
- `sudo reboot`

after reboot

- `cat genData.txt` to see if data is being written to file



on odroid08
crontab = `@reboot sudo sh /home/odroid/runDataDump.sh`

#@reboot sudo python3 /home/odroid/dataDump.py
@reboot sudo sh /home/odroid/runDataDump.sh

sh file:
```
#!/bin/sh
# runDataDump.sh
# Navigate to home directory, then to this directory.
# Then execute python script
# Then navigate back to home


cd /
python3 /home/odroid/dataDump.py


```



- All SBCs reset to new standard and test started @: 

## TEST 2 Log




## Results - Test 1

As Of:
- 16:56 09/01/2023 - All Hosts Alive
- 09:42 10/01/2023 - All Hosts alive
- 16:42 10/01/2023 - All Hosts Alive
- 11:14 11/01/2023 - All Hosts Alive
- 16:52 11/01/2023 - All Hosts Alive
- 10:00 12/01/2023 - All Hosts Alive
- 13:00 12/01/2023 - All Hosts Alive
- 16:29 12/01/2023 - All Hosts Alive
- 10:22 13/01/2023 - All Hosts Alive

TEST 1 FINSIHED


|SBC hostname |  Still Active | If Inactive, Last known time of Operation |
|---|---|---|


## Test 2