package twelve

import (
	"fmt"
	"strings"
)

var days = []string{
	"Zero",
	"first",
	"second",
	"third",
	"fourth",
	"fifth",
	"sixth",
	"seventh",
	"eighth",
	"ninth",
	"tenth",
	"eleventh",
	"twelfth",
}

var dayParts = []string{
	"junk string",
	"a Partridge in a Pear Tree",
	"two Turtle Doves",
	"three French Hens",
	"four Calling Birds",
	"five Gold Rings",
	"six Geese-a-Laying",
	"seven Swans-a-Swimming",
	"eight Maids-a-Milking",
	"nine Ladies Dancing",
	"ten Lords-a-Leaping",
	"eleven Pipers Piping",
	"twelve Drummers Drumming",
}

// Verse returns the verse
func Verse(day int) string {
	songPrefix := generatePrefix(day)
	songPostfix := generatePostfix(day)

	return songPrefix + " " + songPostfix + "."
}

// using a static string with formatter
var commonPart = "On the %s day of Christmas my true love gave to me:"

func generatePrefix(day int) string {
	return fmt.Sprintf(commonPart, days[day])
}

func generatePostfix(day int) string {
	if day == 1 {
		return dayParts[1]
	}

	postfix := ""
	for i := day; i > 1; i-- {
		postfix += dayParts[i] + ", "
	}

	postfix += fmt.Sprintf("and %s", dayParts[1])
	return postfix
}

// using memoization
var song string = ""

// Song returns song
// It memoize the Song, so that we can return the cache
func Song() string {
	if song == "" {
		for day := 1; day < len(days); day++ {
			song += Verse(day) + "\n"
		}
	}

	song = strings.TrimSpace(song)
	return song
}
