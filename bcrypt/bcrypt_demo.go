package main

import (
	"fmt"

	"golang.org/x/crypto/bcrypt"
)

func main()  {
	// 哈希密码
	password := "123456"
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		panic(err)
	}
	fmt.Printf("encryptedPassword is %s\n", string(hashedPassword))

	// 验证密码
	encryptedPassword := hashedPassword
	expectedPassword := password
	err = bcrypt.CompareHashAndPassword([]byte(encryptedPassword), []byte(expectedPassword))
	if err != nil {
		panic(err)
	}
	fmt.Printf("[MATCH]password is %s\n", expectedPassword)
}