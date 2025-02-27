from stats import get_num_words, get_frequency, get_dict
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()
        return file
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    frequency = get_dict(get_frequency(text))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in frequency:
        print(f"{entry['char']}: {entry['freq']}")
main()