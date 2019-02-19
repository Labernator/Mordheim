export GOPATH=/home/klaute/Mordheim/Bastelbrothers/toolheim/
GOOS=linux GOARCH=386 go build -o toolheim386.bin . # linux 32bit binary
GOOS=windows GOARCH=386 go build -o toolheim.exe . # windows binary
GOOS=linux GOARCH=amd64 go build -o toolheim.bin . # linux binary
