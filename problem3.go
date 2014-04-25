// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143 ?

package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	for i := 3; i <= int(math.Sqrt(float64(n)) + 1); i++ {
		if n % i == 0 {
			return false
		}
	}
	return true
}

func main() {
	n := 600851475143
	m := 1
	for n > 1 {
		m += 2
		if isPrime(m) {
			for n % m == 0 {
				n = n / m
			}
		}
	}
	fmt.Printf("%d", m)
}
