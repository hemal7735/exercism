package flatten

// Flatten returns
func Flatten(input interface{}) []interface{} {
	result := []interface{}{}
	
	// Type Switches -> https://tour.golang.org/methods/16
	switch val := input.(type) {
	case int:
		result = append(result, val)
	case []interface{}:
		for _, item := range val {
			result = append(result, Flatten(item)...)
		}
	}

	return result
}