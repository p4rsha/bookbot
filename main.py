from stats import get_num_words, get_book_text, char_count, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    
    book_path = sys.argv[1]
    frank_text = get_book_text(book_path)
    word_count = get_num_words(frank_text)
    char_count_dict = char_count(frank_text)
    sorted_dict_list = sort_dict(char_count_dict)


    # report

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    for item in sorted_dict_list:
        
        if item["char"].isalpha():

         print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

   
main()