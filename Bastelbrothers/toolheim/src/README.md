# Toolheim

A simple tool to generate warband roasters out of .mordheim definition
files.

## Building
    > export GOPATH=/complete/path/to/Bastelbrothers/toolheim/
    > go get github.com/jung-kurt/gofpdf
    > go get github.com/ghodss/yaml
    > GOOS=windows GOARCH=386 go build -o toolheim.exe . # windows binary
    > GOOS=linux GOARCH=amd64 go build -o toolheim.bin . # linux binary
    > GOOS=darwin GOARCH=arm64 go build -o toolheim.app . # OSX binary

## Usage

General help:

    > ./toolheim.bin --help

Generate the PDF (warband-roaster.pdf) from a .mordheim file:

    > ./toolheim.bin -warband aaron.mordheim
