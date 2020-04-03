package main

import (
    "net/http"
    "time"
    "log"
)

func main() {
    s := &http.Server{
        Addr:   ":1323",
        ReadTimeout: 10 * time.Second,
        WriteTimeout: 10 * time.Second,
        MaxHeaderBytes: 1 << 20,
    }

    http.HandleFunc("/", myHandler)

    log.Fatal(s.ListenAndServe())
}

func myHandler(w http.ResponseWriter, r *http.Request){
        w.Write([]byte("Hello World"))
}
