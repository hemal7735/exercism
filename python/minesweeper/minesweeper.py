def annotate(minefield):
    # Function body starts here
    rows = len(minefield)
    if rows == 0:
        return minefield
    
    cols = len(minefield[0])
    if cols == 0:
        return minefield

    # check if the board has the same length in every row
    for row in minefield:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")    

    # print(rows, cols)
    
    directions = [[0,-1], [0,1], [-1, 0], [1, 0], [1,1], [-1,-1], [1,-1], [-1,1]]

    resolved_fieled = []

    def has_mine(_rows, _cols, _r, _c, field):
        if _r < 0 or _c < 0 or _r >= _rows or _c >= _cols:
            return False
        print("passed row,col:", _r, _c)
        return field[_r][_c] == '*'

    for r in range(0, rows):
        resolved_row = ''
        
        for c in range(0, cols):
            
            place = minefield[r][c]

            if place == '*':
                resolved_row += '*'
            elif place != ' ':
                raise ValueError("The board is invalid with current input.")
            else:
                mines = 0
                print('calc for: [r:c]', r, c)
                for d in directions:
                    if has_mine(rows, cols, r + d[0], c + d[1], minefield):
                        mines += 1
                
                if mines == 0:
                    resolved_row += ' '
                else:
                    resolved_row += str(mines)

        resolved_fieled.append(resolved_row)
                           
    return resolved_fieled
