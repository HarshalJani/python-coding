
class Books:
    def __init__(self, title: str, author: str, genre: str, rating: float):
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating


class LibraryManagement:
    def __init__(self):
        self.inventory = []


    def add_books(self, book):
        self.inventory.append(book)

    
    def show_inventory(self):
        book_dict = {}
        for book in self.inventory:
            book_dict['title'] = book.title
            book_dict['author'] = book.author
            book_dict['genre'] = book.genre
            book_dict['rating'] = book.rating
            print(book_dict)


    def get_top_rated_book(self, n: int):
        if not self.inventory:
            return None
        
        books_by_rating = sorted(self.inventory, key = lambda book: book.rating, reverse= True)
        return books_by_rating[:n]
    

    def recommend_top_three_books_by_genre(self, genre: str):
        if not self.inventory:
            return None
        
        books_by_genre = [book for book in self.inventory if book.genre == genre] 
        top_books_by_genre = sorted(books_by_genre, key= lambda b: b.rating, reverse= True)

        return top_books_by_genre[:3] if len(top_books_by_genre) >= 3 else top_books_by_genre

if __name__ == "__main__":

    book1 = Books("Harry Potter and the Sorcerer's Stone", "J.K Rowling", "Fiction", 9.5)
    book2 = Books("Alchemist", "Paulo Coelho", "Adventure", 7.5)
    book3 = Books("Winds of Winter", "George R.R. Martin", "Fiction", 8.9)
    book4 = Books("Death on the Nile", "Agatha Christie", "Thriller", 9.2)
    book5 = Books("To Kill a Mocking Bird", "Harper Lee", "Thriller", 8.5)
    book6 = Books("A Game of Thrones", "George R.R. Martin", "Fiction", 9)

    lib_manage = LibraryManagement()
    lib_manage.add_books(book1)
    lib_manage.add_books(book2)
    lib_manage.add_books(book3)
    lib_manage.add_books(book4)
    lib_manage.add_books(book5)
    lib_manage.add_books(book6)

    print("These are all the books we have")
    lib_manage.show_inventory()

    print("\n")
    print("Top rated books by Readers")
    top_by_rating = lib_manage.get_top_rated_book(3)
    for top_books in top_by_rating:
        print(top_books.title, top_books.rating)

    print("\n")
    print("Based on Thriller Genre here are your top 3 recommendations")
    top_by_genre = lib_manage.recommend_top_three_books_by_genre(genre="Thriller")
    for book_genre in top_by_genre:
        print(book_genre.genre, book_genre.title, book_genre.rating)


