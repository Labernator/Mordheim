@echo off
del warband-roaster.pdf
set TMP_DIR=%cd%
echo %TMP_DIR%
set GOPATH=c:\users\klaute\Dropbox\Privat\tabletop\Mordheim\Bastelbrothers\toolheim\
c:
cd c:\users\klaute\Dropbox\Privat\tabletop\Mordheim\Bastelbrothers\toolheim\src\

toolheim.exe -prj -warband "%TMP_DIR%"\kai.mordheim_post7.yml > tmp.json

move warband-roaster.pdf "%TMP_DIR%"

pause
