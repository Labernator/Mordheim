@echo off
del warband-roaster.pdf
set TMP_DIR=%cd%
echo %TMP_DIR%
set GOPATH=c:\users\klaute\Dropbox\Privat\tabletop\Mordheim\Bastelbrothers\toolheim\
c:
cd c:\users\klaute\Dropbox\Privat\tabletop\Mordheim\Bastelbrothers\toolheim\src\

toolheim.exe -warband "%TMP_DIR%"\orks_n_goblins_n_squigs.mordheim.yml

move warband-roaster.pdf "%TMP_DIR%"

pause
