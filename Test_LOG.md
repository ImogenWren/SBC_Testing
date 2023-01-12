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


## Results

As Of:
- 16:56 09/01/2023 - All Hosts Alive
- 09:42 10/01/2023 - All Hosts alive
- 16:42 10/01/2023 - All Hosts Alive
- 11:14 11/01/2023 - All Hosts Alive
- 16:52 11/01/2023 - All Hosts Alive
- 10:00 12/01/2023 - All Hosts Alive
- 13:00 12/01/2023 - All Hosts Alive
- 16:29 12/01/2023 - All Hosts Alive


|SBC hostname |  Still Active | If Inactive, Last known time of Operation |
|---|---|---|
