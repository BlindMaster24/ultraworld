@echo off
title "Updating is in progress, please do not close this window"
powershell -command "Expand-Archive -Path 'uw-c.zip' -DestinationPath '.' -Force"
del uw-c.zip
start "" uw.exe
exit
