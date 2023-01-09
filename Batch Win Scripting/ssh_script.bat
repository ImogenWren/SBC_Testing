@echo off
title Static IP SHH
:start
echo Attempting Connection with Static IP as user imogen
set choice=
set /p choice="Enter Number of SBC:"
echo Attempting Connection with 192.168.1.'%choice%' as user imogen
ssh imogen@192.168.1."%choice%"
echo Closing Connection...
set choice=
set /p choice="Do you want to restart? Press 'y' and enter for Yes: "
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='y' goto start
pause
