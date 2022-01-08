package letter

// FreqMap records the frequency of each rune in a given text.
type FreqMap map[rune]int

// Frequency counts the frequency of each rune in a given text and returns this
// data as a FreqMap.
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

// ConcurrentFrequency returns FreqMap
func ConcurrentFrequency(texts []string) FreqMap {
	// create a channel to recive individual maps from all the goroutines
	channel := make(chan FreqMap)

	// submit tasks to each goroutine
	for _, text := range texts {
		go func(t string) {
			channel <- Frequency(t)
		}(text)
	}

	result := FreqMap{}

	for range texts {
		// get value from earlier emitted values from the goroutines
		mapFromText := <-channel

		for runeValue, count := range mapFromText {
			result[runeValue] += count
		}
	}

	return result
}
