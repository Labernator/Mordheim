@echo off
del warband-roaster.pdf
set TMP_DIR=%cd%
echo %TMP_DIR%
set GOPATH=c:\users\klaute\Dropbox\Privat\Mordheim\Bastelbrothers\toolheim\
c:
cd c:\users\klaute\Dropbox\Privat\Mordheim\Bastelbrothers\toolheim\src\
rem toolheim.exe -prj -warband tmp.json
rem toolheim.exe -prj -warband "%TMP_DIR%"\kai.mordheim_post6.yml > tmp.json
toolheim.exe -prj -warband "%TMP_DIR%"\kai.mordheim_post5.yml > tmp.json
rem go run main.go -warband "%TMP_DIR%"\kai.mordheim_post4.yml
move warband-roaster.pdf "%TMP_DIR%"

pause
