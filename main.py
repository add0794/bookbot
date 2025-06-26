from stats import Book
import sys

args = sys.argv

if len(args) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = Book(args[1])
book.get_book_text()
# print(book.count_words())
print(book.count_characters())
print(book.sort_characters())
# print(book.report())