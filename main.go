package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	args := os.Args

	//testing in prep for getting the PE
	b, err := ioutil.ReadFile(args[1]) // just pass the file name
	if err != nil {
		fmt.Print(err)
	}

	fmt.Println(b) // print the content as 'bytes'

	str := string(b) // convert content to a 'string'

	fmt.Println(str) // print the content as a 'string'
}
