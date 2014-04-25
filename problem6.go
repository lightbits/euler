// The sum of the squares of the first ten natural numbers is,

// 1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is,

// (1 + 2 + ... + 10)^2 = 552 = 3025
// Hence the difference between the sum of the squares of the first 
// ten natural numbers and the square of the sum is 3025 − 385 = 2640.

// Find the difference between the sum of the squares of the first 
// one hundred natural numbers and the square of the sum.

//////////////
// Solution //
//////////////

package main
import "fmt"

func main() {
	sum_squares := 0
	square_sum := 0
	for n := 1; n <= 100; n++ {
		sum_squares += n * n
		square_sum += n
	}
	square_sum *= square_sum
	fmt.Printf("%d", square_sum - sum_squares)
}