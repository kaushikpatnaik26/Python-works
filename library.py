# LIBRARY MANAGEMENT SYSTEM
class Library:
    def __init__(self):
        self.books = {"Python programming":True,
                      "Introduction to Java":True,
                      "Web development & design":True,
                      "Data Structures & Algorithms":True}
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("")
            print("===== Books available =====\n")
            for book, status in self.books.items():
                print(f"{book}")
    
    def issue_book(self, book):
        if book in self.books and self.books[book]:
            self.books[book] = False
            print(f"You have successfully borrowed '{book}'.")
        else:
            print(f"'{book}' is not found in the library.")
    
    def return_book(self, book):
        if book in self.books and not self.books[book]:
            self.books[book] = True
            print(f"Thank you for returning '{book}'.")
        else:
            print(f"'{book}' is not found in the library.")
    
    def add_book(self, book):
        if book in self.books:
            print(f"'{book}' is already in the library.")
        else:
            self.books[book] = True
            print(f"'{book}' has been added to the library.")
    
    def show_menu(self):
        while True:
            print("\n===== LIBRARY MENU =====")
            print("1. Display available books")
            print("2. Issue a book")
            print("3. Return a book")
            print("4. Add a book")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.display_books()
            elif choice == '2':
                book = input("Enter the name of the book you want to issue: ")
                self.issue_book(book)
            elif choice == '3':
                book = input("Enter the name of the book you want to return: ")
                self.return_book(book)
            elif choice == '4':
                book = input("Enter the name of the book you want to add: ")
                self.add_book(book)
            elif choice == '5':
                print("Thank you! Have a good day.")
                break
            else:
                print("Invalid choice.")

def main():
    library = Library()
    library.show_menu()

if __name__ == "__main__":
    main()


