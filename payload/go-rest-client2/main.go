package main

import (
	"context"
	"fmt"
	"log"

	"golang.org/x/oauth2"
)

func main() {
	var conf = oauth2.Config{
		ClientID:     "QzNIO71KLpdlEyGtF48H4oYrRfAa",
		ClientSecret: "JSaoAKcx5Y_wgJh0fecR3Bhf0lwa",
		Scopes:       []string{"refresh_token"},
		RedirectURL:  "https://192.168.50.24:8243/myapione/0.1.0",
		Endpoint: oauth2.Endpoint{
			AuthURL:  "https://192.168.50.24:8243/authorize",
			TokenURL: "https://192.168.50.24:9443/oauth2/token",
		},
	}
	code := "UXpOSU83MUtMcGRsRXlHdEY0OEg0b1lyUmZBYTpKU2FvQUtjeDVZX3dnSmgwZmVjUjNCaGYwbHdh"
	token, err := conf.Exchange(context.Background(), code)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println("token:", token)

}
