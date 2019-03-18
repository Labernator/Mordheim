set GOPATH=c:\users\klaute\Dropbox\Privat\Mordheim\Bastelbrothers\toolheim\

rem ***** linux 32bit binary *****

set GOOS=linux
set GOARCH=386
go build -o toolheim386.bin .

rem ***** windows binary *****
set GOOS=windows
set GOARCH=386
go build -o toolheim.exe .

rem ***** linux binary *****

set GOOS=linux
set GOARCH=amd64
go build -o toolheim.bin .

pause

