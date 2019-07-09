@echo off
del warband-roaster.pdf
set TMP_DIR=%cd%
echo %TMP_DIR%
set GOPATH=c:\users\klaute\Dropbox\Privat\Mordheim\Bastelbrothers\toolheim\
c:
cd c:\users\klaute\Dropbox\Privat\Mordheim\Bastelbrothers\toolheim\src\

toolheim.exe -prj -warband "%TMP_DIR%"\forest_goblins_pre_20.yml > tmp.json

move warband-roaster.pdf "%TMP_DIR%"\warband-roaster_20.pdf

pause
