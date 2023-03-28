@echo off
title SSH imogen@raspberrypi[HOST]
:start
echo Attempting Connection with HOSTNAME
::set userName=
::set /p userName="Enter SBC User:  "
::echo User Set "%userName%"
set sbcNum=
set /p sbcNum="Enter Number of SBC:  "
echo Attempting Connection with raspberrypi%sbcNum%.local as user imogen
echo ssh imogen@raspberrypi%sbcNum%.local
ssh imogen@raspberrypi%sbcNum%.local
echo Closing Connection...
timeout /t 10
set choice=
set /p choice="Do you want to restart? Press 'y' and enter for Yes: "
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='y' goto start
pause