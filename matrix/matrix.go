package matrix

import "strings"

import "fmt"

import "strconv"

// Matrix returns the Matrix type
type Matrix struct {
	rows [][]int
}

// Rows returns matrix in a rows format
func (m *Matrix) Rows() [][]int {
	result := make([][]int, len(m.rows))

	for i, val := range m.rows {
		result[i] = make([]int, len(val))
		copy(result[i], val)
	}
	return result
}

// Cols returns matrix  in a cols format
func (m *Matrix) Cols() [][]int {

	rowsCount := len(m.rows)
	colsCount := len(m.rows[0]) // we have same columns in all rows

	// we will create a transpose of a matrix (r, c) -> (c, r)
	resultMat := make([][]int, colsCount)

	for i := range resultMat {
		resultMat[i] = make([]int, rowsCount)
	}

	// transpose
	for rowIdx := 0; rowIdx < rowsCount; rowIdx++ {
		for colIdx := 0; colIdx < colsCount; colIdx++ {
			resultMat[colIdx][rowIdx] = m.rows[rowIdx][colIdx]
		}
	}
	return resultMat
}

// Set sets the value at [row, col]
func (m *Matrix) Set(row int, col int, val int) bool {
	rowsCount := len(m.rows)
	colsCount := len(m.rows[0])

	if row < 0 || row > rowsCount-1 || col < 0 || col > colsCount-1 {
		return false
	}

	m.rows[row][col] = val

	return true
}

// New returns the object
func New(input string) (*Matrix, error) {
	result := new(Matrix)

	var colsCount = 0

	var lines = strings.Split(input, "\n")

	for rowIdx, line := range lines {

		var tokens []string = parseLine(line)
		var foundCols = len(tokens)

		// reject if it is empty line
		if foundCols == 0 {
			return nil, fmt.Errorf("Empty Line Found at %d", rowIdx+1)
		}

		// take the cols count in the first rows as a reference to verify balanced matrix
		if colsCount == 0 {
			colsCount = foundCols
		}

		// for all next iterations, we will check if the colsCount is same as we registered earlier
		if foundCols != colsCount {
			return nil, fmt.Errorf("Matrix is not balanced, expected:%d, but found %d", colsCount, foundCols)
		}

		// it is all good now.
		// It is always better to pre-allocate the memory if we know the size upfront
		result.rows = append(result.rows, make([]int, colsCount))

		for colIdx, token := range tokens {
			col, err := strconv.Atoi(token)

			// we could not convert token to integer
			if err != nil {
				return nil, fmt.Errorf("Col %s cannot be converted to integer on row: %d", token, rowIdx+1)
			}

			result.rows[rowIdx][colIdx] = col
		}
	}

	return result, nil
}

// parseLine parses each line and returns the tokens
func parseLine(line string) []string {
	line = strings.TrimSpace(line)

	var tokens = []string{}

	for _, token := range strings.Split(line, " ") {
		tokens = append(tokens, token)
	}

	return tokens
}
