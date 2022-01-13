import string

def is_pangram(sentence):
    letters = set(string.ascii_lowercase)

    return set(sentence.lower()).issuperset(letters)    
