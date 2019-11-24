package hamming

import "errors"

// Distance returns the hamming_distance, error
func Distance(a, b string) (int, error) {

	if len(a) != len(b) {
		return 0, errors.New("Length of a and Length of b does not match")
	}

	dist := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			dist++
		}
	}

	return dist, nil
}
