package main

import (
	"bufio"
	"encoding/json"
	"errors"
	"fmt"
	"os"
)

func main() {
	addressMap := make(map[string]string)
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Enter a name")
	scanner.Scan()
	line := scanner.Text()

	fmt.Println(line)
	addressMap["name"] = line

	fmt.Println("Enter an address")
	scanner.Scan()
	line = scanner.Text()
	addressMap["address"] = line

	jsonValue, err := json.Marshal(addressMap)

	if err != nil {
		panic(errors.New("could not create json"))
	}
	fmt.Println(string(jsonValue))

}
