package accumulate

// Accumulate blah blah
func Accumulate(texts []string, op func(string) string) []string {

	// always better to pre-allocate memory
	var result = make([]string, len(texts))

	for i, text := range texts {
		result[i] = op(text)
	}
	return result
}
