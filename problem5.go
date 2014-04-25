// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

//////////////
// Solution //
//////////////

package main
import "fmt"

func isDivisible(n int) bool {
	for k := 2; k <= 20; k++ {
		if n % k != 0 {
			return false
		}
	}
	return true
}

func main() {
	n := 20
	for {
		if isDivisible(n) {
			fmt.Printf("%d", n)
			break
		}
		n += 1
	}
}