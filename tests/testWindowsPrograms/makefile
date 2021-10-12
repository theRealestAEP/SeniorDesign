BINARY_NAME=testEXE.exe
 
build:
	GOOS=windows GOARCH=amd64 go build -o ${BINARY_NAME} main.go

clean:
	go clean
	rm ${BINARY_NAME}