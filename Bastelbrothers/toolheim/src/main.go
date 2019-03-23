package main

import (
	"flag"
	"io/ioutil"

	"toolheim"
	"fmt"
	"github.com/ghodss/yaml"
)

var warbandFile = flag.String("warband", "", ".mordheim warband definition file to work with")
var multiPage = flag.Bool("multipage", false, ".flag to generate multipage PDF")
var prJSON = flag.Bool("prj", false, ".print json representation")

func main() {
	flag.Parse()

	yamlContent, err := ioutil.ReadFile(*warbandFile)
	if err != nil {
		panic(err)
	}

	warband := toolheim.ParseWarband(yamlContent)
	//fmt.Println(warband.Rating)
	toolheim.MakePDF(warband, *multiPage)

	if *prJSON {
		j, err := yaml.YAMLToJSON(yamlContent)
		if err != nil {
			panic(err)
		}
		fmt.Println(string(j))
	}
}
