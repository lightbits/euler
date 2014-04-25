// Each new term in the Fibonacci sequence is generated 
// by adding the previous two terms. By starting with 1 and 2, 
// the first 10 terms will be:

// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

// By considering the terms in the Fibonacci sequence whose values 
// do not exceed four million, find the sum of the even-valued terms.

//////////////
// Solution //
//////////////

package main
import "fmt"

func main() {
	f0 := 0
	f1 := 1
	sum := 0
	for f1 <= 4000000 {
		f := f0 + f1
		f0 = f1
		f1 = f
		if f % 2 == 0 {
			sum += f
		}
	}
	fmt.Printf("%d", sum)
}