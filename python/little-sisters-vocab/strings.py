def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    ans = prefix

    for item in vocab_words[1:]:
        ans += " :: " + prefix + item

    return ans

def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    last_letter = word[-5]
    last_last_letter = word[-6]

    print("string is:", word)
    print("last letter is:" + last_letter)
    print("last_last_letter is:" + last_last_letter)

    def is_vowel(letter):
        return letter in ['a', 'e', 'i', 'o', 'u']

    if last_letter == 'i' and not is_vowel(last_last_letter) :
        return word[0:-5] + 'y'
    
    return word[0:-4]


def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    words = sentence[:-1].split(" ")

    return words[index] + 'en'
