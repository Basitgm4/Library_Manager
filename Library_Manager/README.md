# Personal Book Library Manager

This is a web application built using Streamlit to manage your personal book library. You can add, view, search, update, and delete book information through an interactive web interface.

## Features

* **Add Books:** Easily add new books with details like title, author, ISBN, genre, publication year, and status.
* **View Books:** See a list of all the books in your library.
* **Search Books:** Search for books by title or author.
* **Update Books:** Modify the information of existing books.
* **Delete Books:** Remove books from your library.
* **Data Persistence:** Book data is saved to a `book_data.json` file, so your library is preserved between sessions.
* **Interactive Web Interface:** Built using Streamlit for an easy-to-use and responsive web application.

## How to Run

1.  **Save the files:** Make sure you have the `book_library_manager` directory with `app.py` (the modified `main.py` code) and `book_data.json` in it.
2.  **Open your terminal or command prompt.**
3.  **Navigate to the `book_library_manager` directory.**
4.  **Run the Streamlit app:** Execute the `app.py` file using the Streamlit command:
    ```bash
    streamlit run app.py
    ```
5.  **Your web browser should automatically open** with the book library manager application. If not, you can open your browser and go to the URL provided in the terminal (usually `http://localhost:8501`).

## Usage

The application provides a sidebar menu on the left:

* **Add Book:** Click to enter the details of a new book.
* **View Books:** Click to see the list of books in your library.
* **Search Book:** Click to search for books by title or author.
* **Update Book:** Click to select and modify the information of an existing book.
* **Delete Book:** Click to select and remove a book from the library.

## Future Enhancements (Possible additions)

* Implement more sophisticated search options (e.g., by genre, year).
* Add the ability to mark books as read or unread.
* Add the option to sort books by different criteria.
* Implement error handling for invalid input more robustly.

## Technologies Used

* Python
* Streamlit
* JSON

## Author

[Your Name/Organization Name]

## License

[Specify your license if you want to open-source it]