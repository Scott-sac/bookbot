from stats import count_words, count_characters, list_dict
import sys

def get_book_text(fpath):
    with open(fpath) as f:
        file_content = f.read()
    return file_content

def main(path):
    text = get_book_text(path) # <-- path to book removed from here
    num_words = count_words(text)
    num_characters = count_characters(text)
    list_characters = list_dict(num_characters)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for i in range(0, len(list_characters)):
        print(f"{list_characters[i].get("letter")}: {list_characters[i].get("num")}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]
    main(file_path)