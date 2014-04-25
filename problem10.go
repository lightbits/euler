// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

// Find the sum of all the primes below two million.

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
	sum := 2 // starting from 3
	for n := 3; n <= 2000000; n += 2 {
		if isPrime(n) {
			sum += n
		}
	}
	fmt.Printf("%d", sum)
}