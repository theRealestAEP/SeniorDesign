build64:
	GOOS=windows GOARCH=amd64 go build -o testEXE64.exe main.go

build32:
	GOOS=windows GOARCH=386 go build -o testEXE32.exe main.go

clean32:
	go clean
	rm testEXE32.exe

clean64:
	go clean
	rm testEXE64.exe

cleanAll:
	go clean
	rm testEXE64.exe
	rm testEXE32.exe