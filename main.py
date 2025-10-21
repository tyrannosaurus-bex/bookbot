import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

from stats import count_words, count_char, sorted_list

def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        file_contents = f.read() 
        return file_contents

def main():
    text = get_book_text(path)
    num_word = count_words(text)
    char_dict = count_char(text)
    sort_list = sorted_list(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    for obj in sort_list:
        print(f"{obj['char']}: {obj['num']}")
    print("============= END ===============")

main()



