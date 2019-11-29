package diffsquares

// Difference return Difference of SquareOfSum and SumOfSquares
func Difference(n int) int {

	first, second := SumOfSquares(n), SquareOfSum(n)

	var result int

	// bigger one is always squareOfSum
	// smaller one is always sumOfSquares
	if first > second {
		result = first - second
	} else {
		result = second - first
	}

	return result
}

// SumOfSquares returns sum-of-squares
func SumOfSquares(n int) int {
	result := (n * (n + 1) * (2*n + 1)) / 6

	return result
}

// SquareOfSum returns square-of-sum
func SquareOfSum(n int) int {

	sum := (n * (n + 1)) / 2
	result := sum * sum

	return result
}
