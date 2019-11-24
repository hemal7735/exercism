package isogram

import (
	"strings"
	"unicode"
)

// IsIsogram checks if the word is an isogram or not
func IsIsogram(word string) bool {
	seen := make(map[rune]bool)

	result := true

	for _, char := range strings.ToUpper(word) {

		if !unicode.IsLetter(char) {
			continue
		}

		if !seen[char] {
			seen[char] = true
		} else {
			result = false
			break
		}
	}

	return result
}
