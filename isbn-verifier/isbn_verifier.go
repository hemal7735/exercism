package isbn

import "strings"

// IsValidISBN checks if the ISBN is valid or not
// A valid ISBN has the following props
// 1. It must be only 10 digits ranging from 0-9 inclusive and X
// 2. X can only appear as a check digit, means that it can only be a last letter
// 3. Cannot have a junk character
// 4. Checksum should be a multiple of 11 means that (checksum mod 11 = 0)
func IsValidISBN(isbn string) bool {

	// basic valiation
	if isbn == "" {
		return false
	}
	sanitizedInput := sanitizeInput(isbn)
	runePoints := []rune(sanitizedInput)

	// validation #1
	if len(runePoints) != 10 {
		return false
	}

	checksum := 0

	for i, runePoint := range runePoints {

		// validation #2
		if runePoint == 'X' && i != 9 {
			return false
		}

		runePointVal := mapRunePointToVal(runePoint)

		// validation #3
		if runePointVal == -1 {
			return false
		}

		checksum += (10 - i) * runePointVal // 0th based index
	}

	// validation #4
	return isValidChecksum(checksum)
}

func isValidChecksum(checksum int) bool {
	return checksum%11 == 0
}

func mapRunePointToVal(runePoint rune) int {
	switch runePoint {
	case 'X':
		return 10
	case '9':
		return 9
	case '8':
		return 8
	case '7':
		return 7
	case '6':
		return 6
	case '5':
		return 5
	case '4':
		return 4
	case '3':
		return 3
	case '2':
		return 2
	case '1':
		return 1
	case '0':
		return 0
	default:
		return -1
	}
}

func sanitizeInput(input string) string {
	var result string

	result = strings.ReplaceAll(input, "-", "")

	// can log the result here, skipping for a now
	return result
}
