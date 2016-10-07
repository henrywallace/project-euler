package main

import "fmt"

func collatz(n int) int {
    if n % 2 == 0 {
        return n/2
    } else {
        return 3*n + 1
    }
}

func main() {
    // lens := make(map[int] int)  // map from number to length of sequence
    // max_length := 0
    for n := 1; n < 1e6; n++ {
        if length, ok := lengths[n]
    }
}   