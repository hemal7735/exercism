package reverse

// Reverse returns the reverse of the input string
func Reverse(str string) string {
	if str == "" {
		return ""
	}

	result := []rune(str)

	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	return string(result)

}
