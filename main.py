from stats import count_words, count_char, sort_key
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

#def count_words(text):
#    words = text.split()
#    num_words = len(words)
#    print(f"{num_words} words found in the document", num_words)
#    return num_words

def main():
    print("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------")
    text = get_book_text(path)
    #print(text)
    count_words(text)
    print("--------- Character Count -------")
    chars = count_char(text)
    sorted_chars = sorted(chars.items(), reverse=True, key=sort_key)
    for letter, count in sorted_chars:
        print(f"{letter}: {count}")
main()
