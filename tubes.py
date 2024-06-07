import time
from itertools import combinations

def brute_force(books, max_time, max_books):
    max_time_minutes = max_time * 60
    best_combination = []
    best_score = 0
    
    for r in range(1, max_books + 1):
        for combo in combinations(books, r):
            total_time = sum(book[1] for book in combo) * 5
            total_rating = sum(book[2] for book in combo)
            
            if total_time <= max_time_minutes and total_rating > best_score:
                best_combination = combo
                best_score = total_rating
                
    return best_combination, sum(book[1] for book in best_combination) * 5

def greedy(books, max_time, max_books):
    max_time_minutes = max_time * 60
    books_sorted = sorted(books, key=lambda x: x[2]/x[1], reverse=True)
    selected_books = []
    total_time = 0
    
    for book in books_sorted:
        if len(selected_books) < max_books:
            book_time = book[1] * 5
            if total_time + book_time <= max_time_minutes:
                selected_books.append(book)
                total_time += book_time
    
    return selected_books, total_time

def format_time(minutes):
    if minutes < 60:
        return f"{minutes} menit"
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours} jam {remaining_minutes} menit"

def get_input():
    while True:
        max_time_input = input("Masukkan jumlah waktu yang dimiliki pustakawan (dalam jam): ")
        try:
            max_time = float(max_time_input)
            if max_time <= 0:
                print("Masukkan jumlah waktu yang valid (bilangan positif).")
            else:
                break
        except ValueError:
            print("Masukkan bilangan yang valid.")

    while True:
        max_books_input = input("Masukkan maksimal buku yang dapat dipinjam oleh pustakawan: ")
        try:
            max_books = int(max_books_input)
            if max_books <= 0:
                print("Masukkan maksimal buku yang valid (bilangan bulat positif).")
            else:
                break
        except ValueError:
            print("Masukkan bilangan bulat yang valid.")

    while True:
        num_books_input = input("Jumlah buku dalam perpustakaan: ")
        try:
            num_books = int(num_books_input)
            if num_books <= 0:
                print("Masukkan jumlah buku yang valid (bilangan bulat positif).")
            else:
                break
        except ValueError:
            print("Masukkan bilangan bulat yang valid.")

    books = []
    for i in range(num_books):
        book_name = input(f"Masukkan nama Buku ke-{i+1}: ")
        while True:
            book_pages_input = input(f"Jumlah lembar buku {book_name} (setiap lembar akan dikali dengan 5 menit): ")
            try:
                book_pages = int(book_pages_input)
                if book_pages <= 0:
                    print("Masukkan jumlah lembar buku yang valid (bilangan bulat positif).")
                else:
                    break
            except ValueError:
                print("Masukkan bilangan bulat yang valid.")
        
        while True:
            book_rating_input = input(f"Rating buku {book_name} (1-10): ")
            try:
                book_rating = int(book_rating_input)
                if 1 <= book_rating <= 10:
                    books.append((book_name, book_pages, book_rating))
                    break
                else:
                    print("Masukkan rating buku yang valid (1-10).")
            except ValueError:
                print("Masukkan bilangan bulat yang valid.")
    
    return max_time, max_books, books

def main():
    max_time, max_books, books = get_input()

    start_time = time.time()
    best_books_bruteforce, brute_force_time_needed = brute_force(books, max_time, max_books)
    bruteforce_time = time.time() - start_time

    start_time = time.time()
    best_books_greedy, greedy_time_needed = greedy(books, max_time, max_books)
    greedy_time = time.time() - start_time

    print("\nMenggunakan Brute Force:")
    for i, book in enumerate(best_books_bruteforce):
        print(f"{i+1}. {book[0]} dengan durasi {book[1] * 5} menit dan rating {book[2]}")
    print("Total durasi waktu (Brute Force):", format_time(brute_force_time_needed))
    print("Execution time (Brute Force):", bruteforce_time, "seconds")

    print("\nMenggunakan Greedy:")
    for i, book in enumerate(best_books_greedy):
        print(f"{i+1}. {book[0]} dengan durasi {book[1] * 5} menit dan rating {book[2]}")
    print("Total durasi waktu (Greedy):", format_time(greedy_time_needed))
    print("Execution time (Greedy):", greedy_time, "seconds")

if __name__ == "__main__":
    main()
