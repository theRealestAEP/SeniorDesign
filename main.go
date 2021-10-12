package main

import (
	"debug/pe"
	"encoding/binary"
	"fmt"
	"io"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func ioReader(file string) io.ReaderAt {
	r, err := os.Open(file)
	check(err)
	return r
}

func main() {

	if len(os.Args) < 2 {
		fmt.Println("Usage: MDE pe_file")
		os.Exit(1)
	}

	file := ioReader(os.Args[1]) //read in fie from arg
	f, err := pe.NewFile(file)   //define f as a PE file
	check(err)                   //error handling

	var sizeofOptionalHeader32 = uint16(binary.Size(pe.OptionalHeader32{})) //if 32 bit
	var sizeofOptionalHeader64 = uint16(binary.Size(pe.OptionalHeader64{})) // if 64 bit

	var dosheader [96]byte //byte array size of 96
	var sign [4]byte
	file.ReadAt(dosheader[0:], 0)
	var base int64
	if dosheader[0] == 'M' && dosheader[1] == 'Z' {
		signoff := int64(binary.LittleEndian.Uint32(dosheader[0x3c:]))
		//var sign [4]byte
		file.ReadAt(sign[:], signoff)
		if !(sign[0] == 'P' && sign[1] == 'E' && sign[2] == 0 && sign[3] == 0) {
			fmt.Printf("Invalid PE File Format.\n")
		}
		base = signoff + 4
	} else {
		base = int64(0)
	}

	sr := io.NewSectionReader(file, 0, 1<<63-1)
	sr.Seek(base, io.SeekStart)
	binary.Read(sr, binary.LittleEndian, &f.FileHeader)

	var oh32 pe.OptionalHeader32
	var oh64 pe.OptionalHeader64
	var x86_x64 string
	var magicNumber uint16

	switch f.FileHeader.SizeOfOptionalHeader {
	case sizeofOptionalHeader32:
		binary.Read(sr, binary.LittleEndian, &oh32)
		if oh32.Magic != 0x10b { // PE32
			fmt.Printf("pe32 optional header has unexpected Magic of 0x%x", oh32.Magic)
		}
		magicNumber = oh32.Magic
		x86_x64 = "x86"

	case sizeofOptionalHeader64:
		binary.Read(sr, binary.LittleEndian, &oh64)
		if oh64.Magic != 0x20b { // PE32+
			fmt.Printf("pe32+ optional header has unexpected Magic of 0x%x", oh64.Magic)
		}
		magicNumber = oh64.Magic
		x86_x64 = "x64"
	}

	var isDLL bool
	if (f.Characteristics & 0x2000) == 0x2000 {
		isDLL = true
	} else if (f.Characteristics & 0x2000) != 0x2000 {
		isDLL = false
	}

	var isSYS bool
	if (f.Characteristics & 0x1000) == 0x1000 {
		isSYS = true
	} else if (f.Characteristics & 0x1000) != 0x1000 {
		isSYS = false
	}

	f.Close() //close file handle

	fmt.Printf("OptionalHeader: %#x\n", f.OptionalHeader)
	fmt.Printf("DLL File: %t\n", isDLL)
	fmt.Printf("SYS File: %t\n", isSYS)
	fmt.Printf("Base: %d\n", base)
	fmt.Printf("File type: %c%c\n", sign[0], sign[1])
	fmt.Printf("dosheader[0]: %c\n", dosheader[0])
	fmt.Printf("dosheader[1]: %c\n", dosheader[1])
	fmt.Printf("MagicNumber: %#x (%s)\n", magicNumber, x86_x64)

}
