from stats import num_of_words, count_characters, print_pretty
import sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content

def main(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")

    text = (get_book_text(path))
    print("----------- Word Count ----------")
    print(f'Found {num_of_words(text)} total words')
    
    print("--------- Character Count -------")
    string_count = count_characters(text)
    sorted_pretty = (print_pretty(string_count))
    for item in sorted_pretty:
        if item["Character"].isalpha() == False:
            continue
        print(f"{item['Character']}: {item['Count']}")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]
main(path)