def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = sorted(word_lower)
    word_len = len(sorted_word)

    ans = []
    
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower == word_lower:
            continue
        
        if len(candidate) == word_len and sorted(candidate_lower) == sorted_word:
                ans.append(candidate)

    return ans
