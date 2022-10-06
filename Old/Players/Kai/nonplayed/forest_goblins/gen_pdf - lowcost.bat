@echo off
del warband-roaster_lowcost.pdf
set TMP_DIR=%cd%
echo %TMP_DIR%
set GOPATH=c:\users\klaute\Dropbox\Privat\tabletop\Mordheim\Bastelbrothers\toolheim\
c:
cd c:\users\klaute\Dropbox\Privat\tabletop\Mordheim\Bastelbrothers\toolheim\src\

toolheim.exe -prj -warband "%TMP_DIR%"\forest_goblins_pre_lowcost.yml > tmp.json

move warband-roaster.pdf "%TMP_DIR%"\warband-roaster_lowcost.pdf

pause
