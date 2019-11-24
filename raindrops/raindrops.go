package raindrops

import (
	"strconv"
)

// Convert return the string
func Convert(input int) string {
	ans := ""

	if input%3 == 0 {
		ans += "Pling"
	}

	if input%5 == 0 {
		ans += "Plang"
	}

	if input%7 == 0 {
		ans += "Plong"
	}

	if len(ans) == 0 {
		ans = strconv.Itoa(input)
	}

	return ans
}
