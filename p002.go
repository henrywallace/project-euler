package main

import (
    "fmt"
)

func fib_gen() chan int {
    ch := make(chan int)
    go func() {
        for i, j := 0, 1; ; i, j = i + j, i {
            ch <- i
        }
    }()
    return ch
}

func main() {
    fibs := fib_gen()
    sum := 0
    for f := <-fibs; f < int(4e6); f = <-fibs {
        if f % 2 == 0 {
            sum += f
        }
    }
    fmt.Println(sum)
}