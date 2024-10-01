import requests
import os
import json
import csv
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_BOOKS_API_KEY")

def get_books(genre, total_books):
    books = []
    max_results_per_request = 40
    start_index = 0
    
    while len(books) < total_books:
        remaining_books = total_books - len(books)
        max_results = min(remaining_books, max_results_per_request)
        
        url = f"https://www.googleapis.com/books/v1/volumes?q={genre}&maxResults={max_results}&startIndex={start_index}&key={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            books.extend(data.get("items", []))

            start_index += max_results
        else:
            print(f"Error: {response.status_code}")
            break

    return books

def save_books_to_json(books, filename="books_raw.json"):
    with open(filename, "w") as json_file:
        json.dump(books, json_file, indent=4)
    print(f"Books saved to {filename}")
    
def save_books_to_csv(books, filename="books_raw.csv"):
    with open(filename, mode="w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["raw_data"])

        for book in books:
            writer.writerow([json.dumps(book)])
    print(f"Books saved to {filename}")

genre = "Sci-Fi"
total_books = 50
books = get_books(genre, total_books)

save_books_to_json(books)
save_books_to_csv(books)
