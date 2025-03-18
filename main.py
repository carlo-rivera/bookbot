from stats import count_words, count_character_appearances, dict_parse
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    book_text = get_book_text(book)
    word_count = count_words(book_text)
    character_occurences = count_character_appearances(book_text)
    neat_char_occurences = dict_parse(character_occurences)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for charAndCount in neat_char_occurences:
        print(f"{charAndCount['char']}: {charAndCount['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()