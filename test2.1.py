import csv
import random
import xml.etree.ElementTree as ET


def generate_bibliography(file_path, num_entries=20):
    bibliography = []

    with open(file_path, mode='r', encoding='ISO-8859-1') as file:
        # Set delimiter ';' instead of the default ','
        reader = csv.DictReader(file, delimiter=';')

        records = list(reader)

        selected_records = random.sample(records, num_entries)

        # Generate bibliographic references
        for idx, row in enumerate(selected_records, start=1):
            author = row['Book-Author']
            title = row['Book-Title']
            year = row['Year-Of-Publication']
            bibliography.append(f"{idx}. {author}. {title} - {year}")

    # Save the references in a text file
    with open('bibliography.txt', mode='w', encoding='utf-8') as file:
        for entry in bibliography:
            file.write(entry + '\n')

    print(f"{num_entries} bibliographic references have been created and saved in 'bibliography.txt'.")


def search_books_by_author(file_path, author_name, max_results=10):
    books_found = []  # List to store books that match the author

    with open(file_path, mode='r', encoding='ISO-8859-1') as file:
        # Set delimiter ';' instead of the default ','
        reader = csv.DictReader(file, delimiter=';')

        for row in reader:
            author = row['Book-Author']
            if author_name.lower() in author.lower():
                books_found.append(row)
                if len(books_found) >= max_results:
                    break

    return books_found


def parse_currency_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    currencies = []
    for currency in root.findall('.//currency'):
        name = currency.find('name').text
        value = currency.find('value').text
        currencies.append((name, value))

    for currency in currencies:
        print(f"Currency Name: {currency[0]}, Value: {currency[1]}")


books_file_path = 'books-en.csv'

author_name = input("Enter the author's name: ")

books_by_author = search_books_by_author(books_file_path, author_name)

if books_by_author:
    print(f"\nBooks written by {author_name}:")
    for book in books_by_author:
        print(
            f"Book Title: {book['Book-Title']}, Year of Publication: {book['Year-Of-Publication']}, Publisher: {book['Publisher']}")
else:
    print(f"\nNo books found by the author {author_name}.")

# Generate bibliographic references
generate_bibliography(books_file_path, num_entries=20)

currency_file_path = 'currency.xml'
parse_currency_xml(currency_file_path)
