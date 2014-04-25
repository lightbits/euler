// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

// a^2 + b^2 = c^2
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

//////////////
// Solution //
//////////////

package main
import "fmt"

func main() {
	for a := 1; a <= 1000; a++ {
		for b := a; b <= 1000 - a; b++ {
			for c := b; c <= 1000 - a - b; c++ {
				if a + b + c == 1000 {
					if a * a + b * b == c * c {
						fmt.Printf("%d", a * b * c)
						return
					}
				}
			}
		}
	}
}