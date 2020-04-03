// +build linux

package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	h := make(handler)
	go counter(h)
	if err := http.ListenAndServe(":8000", h); err != nil {
		log.Print(err)
	}
}

func counter(ch chan<- int) {
	for n := 0; ; n++ {
		ch <- n
	}
}

type handler chan int

func (h handler) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-type", "text/plain")
	fmt.Fprintf(w, "%s: you are visitor #%d", req.URL, <-h)
}

func sayHi() error {
	fmt.Println("hi")
	return nil
}

func sayYoo() string {
	return "yoo"
}
