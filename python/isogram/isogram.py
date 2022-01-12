def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').lower()

    letters = set()

    for c in string:
        if c in letters:
            return False
        
        letters.add(c)
    
    return True
