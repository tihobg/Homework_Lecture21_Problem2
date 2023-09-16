import csv
from book import Book
from insert_new_book import insert_new_book

books = [
    Book('0', 'To Kill A Mockingbird', 'Harper Lee', '1960'),
    Book('1', 'A Brief History of Time', 'Stephen Hawking', '1988'),
    Book('2', 'The Great Gatsby', 'F.Scott Fitzgerald', '1922')
]
print([str(b) for b in books])
with open('Book.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([' ', 'Book', 'Author', 'Year Released'])
    for b in books:
        writer.writerow([b.number, b.book, b.author, b.year])
        print(b)

new_book = insert_new_book(books)
print(new_book)
with open('Book.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([' ', 'Book', 'Author', 'Year Released'])
    for b in books:
        writer.writerow([b.number, b.book, b.author, b.year])
    writer.writerow([new_book.number + 1, new_book.book, new_book.author, new_book.year])

with open('Book.csv', 'r') as f:
    reader = csv.reader(f)
    content = [line for line in reader if len(line) > 0]
    print(content)
# with open('Book.csv', 'r') as f:
#     content = f.read()
#     print(content)
#
