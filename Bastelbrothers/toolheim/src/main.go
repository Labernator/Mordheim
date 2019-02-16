package main

import (
	"flag"
	"io/ioutil"

	"toolheim"
)

var warbandFile = flag.String("warband", "", ".mordheim warband definition file to work with")

func main() {
	flag.Parse()

	yamlContent, err := ioutil.ReadFile(*warbandFile)
	if err != nil {
		panic(err)
	}

	warband := toolheim.ParseWarband(yamlContent)
	toolheim.MakePDF(warband)
}
