from stats import get_word_count
from stats import count_characters
from stats import book_dic_sorter
from stats import sort_on
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_location = sys.argv[1]
    with open(file_location) as f:
        book_text = f.read()

    word_count = get_word_count(book_text)
    char_count_dict = count_characters(book_text)
    pre_sorted_list = book_dic_sorter(char_count_dict)
    pre_sorted_list.sort(reverse=True, key=sort_on)
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_location}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for item in pre_sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()