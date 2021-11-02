package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"math"
	"os"
)

func ioReader(file string) io.ReaderAt {
	r, _ := os.Open(file)
	return r
}

func main() {

	if len(os.Args) < 2 {
		fmt.Println("Usage: ENT file_toCompare")
		os.Exit(1)
	}

	buf, _ := ioutil.ReadFile(os.Args[1]) //read in fie from arg

	file := string(buf)

	bits := Shannon(file)

	fmt.Printf("total number of bits: %d\n", bits)

	var ratio_test_1 int = bits / len(file) //set the ratio of bits to length to normalize entropy

	fmt.Printf("shanon entropy ratio: %d\n", ratio_test_1)

}

// Shannon measures the Shannon entropy of a string.
// See http://bearcave.com/misl/misl_tech/wavelets/compression/shannon.html for the algorithmic explanation.
func Shannon(value string) (bits int) {
	frq := make(map[rune]float64)

	//get frequency of characters
	for _, i := range value {
		frq[i]++
	}

	var sum float64

	for _, v := range frq {
		f := v / float64(len(value))
		sum += f * math.Log2(f)
	}

	bits = int(math.Ceil(sum*-1)) * len(value)
	return
}
