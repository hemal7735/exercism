package hamming

import "errors"

// Distance returns the hamming_distance, error
func Distance(a, b string) (int, error) {
	runeA := []rune(a)
	runeB := []rune(b)
	
	if len(runeA) != len(runeB) {
		return 0, errors.New("Length of a and Length of b does not match")
	}

	dist := 0
	for i := 0; i < len(runeA); i++ {
		if runeA[i] != runeB[i] {
			dist++
		}
	}

	return dist, nil
}
