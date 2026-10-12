class BookModel:

    def __init__(self):
        # Начальный список книг
        self.books = [
            {"title": "Системний аналіз", "author": "Петренко В.І."},
            {"title": "Архітектура ПЗ", "author": "Коваленко О.М."},
        ]

    def get_all_books(self):
        return self.books

    def add_book(self, title, author):
        if title.strip() and author.strip():
            self.books.append({"title": title.strip(), "author": author.strip()})
            return True
        return False

class BookView:

    def show_books(self, books):
        print("\n--- СПИСОК КНИГ У БІБЛІОТЕЦІ ---")
        if not books:
            print("Список порожній.")
        for idx, book in enumerate(books, 1):
            print(f"{idx}. Назва: «{book['title']}» | Автор: {book['author']}")
        print("-" * 35)

    def get_book_input(self):
        print("\nВведіть нову книгу:")
        title = input("Назва книги: ")
        author = input("Автор: ")
        return title, author

    def show_message(self, message):
        print(f"[Повідомлення]: {message}")

class BookController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Переглянути список книг")
            print("2. Додати нову книгу")
            print("3. Вихід")

            choice = input("Оберіть дію (1-3): ").strip()

            if choice == "1":
                books = self.model.get_all_books()
                self.view.show_books(books)
            elif choice == "2":
                title, author = self.view.get_book_input()
                success = self.model.add_book(title, author)
                if success:
                    self.view.show_message(
                        "Книгу успішно додано до каталогу!"
                    )
                else:
                    self.view.show_message(
                        "Помилка: поля не можуть бути порожніми."
                    )
            elif choice == "3":
                print("Роботу програми завершено.")
                break
            else:
                self.view.show_message(
                    "Невірний вибір. Спробуйте ще раз (1-3)."
                )

if __name__ == "__main__":
    model = BookModel()
    view = BookView()
    controller = BookController(model, view)
    controller.run()