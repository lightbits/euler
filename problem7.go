// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
// we can see that the 6th prime is 13.

// What is the 10 001st prime number?

//////////////
// Solution //
//////////////

package main
import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	for i := 3; i <= int(math.Sqrt(float64(n))) + 1; i++ {
		if n % i == 0 {
			return false
		}
	}
	return true
}

func main() {
	n := 1
	num_primes := 1 // 2 is prime
	for num_primes < 10001 {
		n += 2
		if isPrime(n) {
			num_primes++
		}
	}
	fmt.Printf("%d", n)
}