# Toolheim

A simple tool to generate warband roasters out of .mordheim definition
files.

## Building
1. Install GoLang for Windows/Linux etc. (https://golang.org/doc/install)
2. Edit all the script files (.sh/.bat) and set your path to the toolheim folder on your harddisc.
3. Start the install modules script (.sh/.bat) and wait. After the installation there are some new folder available.
4. (optional) Run the build script (.sh/.bat) if there is no .exe/.bin file in the git available. Those files will be automatically generated.
5. Edit your warband roster .yml file, copy the example file.
6. Run the gen_pdf script (.sh/.bat) to generate the warband roster PDF.

Manually install on Linux:
1. Open a terminal
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

    > ./toolheim.bin -warband example.mordheim.yml
