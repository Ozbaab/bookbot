from stats import num_of_words, count_characters, print_pretty

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    text = (get_book_text("books/frankenstein.txt"))
    print("----------- Word Count ----------")
    print(f'Found {num_of_words(text)} total words')
    
    print("--------- Character Count -------")
    string_count = count_characters(text)
    sorted_pretty = (print_pretty(string_count))
    for item in sorted_pretty:
        if item["Character"].isalpha() == False:
            continue
        print(f"{item['Character']}: {item['Count']}")

main()