package series

// All returns a list of all substrings of s with length n.
func All(n int, s string) []string {

	var result = []string{}

	for start := 0; start+n <= len(s); start++ {
		result = append(result, s[start:start+n])
	}
	return result
}

// UnsafeFirst returns the first substring of s with length n.
func UnsafeFirst(n int, s string) string {
	return s[0:n]
}

// First - We need a way to signal that in some cases you can't take the first N characters of the string.
// UnsafeFirst can't do that since it only returns a string.
func First(n int, s string) (first string, ok bool) {

	if n > len(s) || n <= 0 {
		return s, false
	}

	return UnsafeFirst(n, s), true

}
