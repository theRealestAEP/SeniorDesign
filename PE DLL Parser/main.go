package main

import (
	"fmt"
	"os"

	"github.com/Binject/debug/pe"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

//"github.com/Binject/debug/pe"

func main() {

	if len(os.Args) < 2 {
		fmt.Println("Usage: MDE pe_file")
		os.Exit(1)
	}

	f, e := pe.Open(os.Args[1])
	check(e)
	defer f.Close()

	a, e := f.ImportedLibraries()
	if e != nil {
		panic(e)
	}
	for _, s := range a {
		println(s)
	}

}