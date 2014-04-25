// A palindromic number reads the same both ways. 
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

//////////////
// Solution //
//////////////

package main
import "fmt"

func isPalindrome(n int) bool {
	digits := make([]int, 0)
	for n > 0 {
		digits = append(digits, n % 10)
		n = n / 10
	}

	for i := 0; i < len(digits) / 2; i++ {
		if digits[i] != digits[len(digits) - 1 - i] {
			return false
		}
	}

	return true
}

func main() {
	answer := 0
	for a := 100; a <= 999; a++ {
		for b := a; b <= 999; b++ {
			p := a * b
			if isPalindrome(p) {
				if p > answer {
					answer = p
				}
			}
		}
	}

	fmt.Printf("%d", answer)
}