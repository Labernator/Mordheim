# Toolheim

A simple tool to generate warband roasters out of .mordheim definition
files.

## Building
1. Install GoLang for Windows/Linux etc. (https://golang.org/doc/install)
2. edit all the script files (.sh/.bat) and set the pth to the toolheim folder
3. start the install modules script (.sh/.bat)
4. run the build script (.sh/.bat) if there is no exe/bin file available
5. edit your warband roster .yml file
6. run the gen_pdf script (.sh/.bat)

Manually on Linux run:
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
