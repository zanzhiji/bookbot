def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
    return num_words

def count_char(text):
    string = text.lower()
    counts = {
    }

    for letter in string:
        if letter.isalpha():
            counts[letter] = counts.get(letter, 0) + 1
    return counts

def sort_key(dictionary):
    return dictionary[1]
