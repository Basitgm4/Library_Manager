# Rename main.py to app.py
import json
import os
import streamlit as st

# Constants
DATA_FILE = "book_data.json"

def load_books():
    """Loads book data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
                return data.get("books", [])
            except json.JSONDecodeError:
                st.error("Error decoding JSON file. Starting with an empty library.")
                return []
    return []

def save_books(books):
    """Saves book data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump({"books": books}, f, indent=4)

def add_book():
    """Adds a new book to the library."""
    st.subheader("Add New Book")
    title = st.text_input("Enter book title:")
    author = st.text_input("Enter author name:")
    isbn = st.text_input("Enter ISBN (optional):")
    genre = st.text_input("Enter genre (optional):")
    publication_year = st.text_input("Enter publication year (optional):")
    status = st.selectbox("Enter status:", ["Available", "Borrowed", "Read"])

    if st.button("Add Book"):
        if title and author:
            book = {
                "title": title,
                "author": author,
                "isbn": isbn if isbn else None,
                "genre": genre if genre else None,
                "publication_year": publication_year if publication_year else None,
                "status": status
            }
            books.append(book)
            save_books(books)
            st.success(f"Book '{title}' by {author} added successfully!")
        else:
            st.warning("Title and Author are required fields.")

def view_all_books():
    """Displays all books in the library."""
    st.subheader("Your Library")
    if not books:
        st.info("Your library is empty.")
        return

    for i, book in enumerate(books):
        st.write(f"--- Book {i + 1} ---")
        st.write(f"**Title:** {book['title']}")
        st.write(f"**Author:** {book['author']}")
        if book.get('isbn'):
            st.write(f"**ISBN:** {book['isbn']}")
        if book.get('genre'):
            st.write(f"**Genre:** {book['genre']}")
        if book.get('publication_year'):
            st.write(f"**Year:** {book['publication_year']}")
        st.write(f"**Status:** {book['status']}")

def search_book():
    """Searches for a book by title or author."""
    st.subheader("Search for Book")
    query = st.text_input("Enter title or author to search:")
    if st.button("Search"):
        if query:
            results = []
            for book in books:
                if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
                    results.append(book)

            if results:
                st.subheader("Search Results")
                for i, book in enumerate(results):
                    st.write(f"--- Result {i + 1} ---")
                    st.write(f"**Title:** {book['title']}")
                    st.write(f"**Author:** {book['author']}")
                    if book.get('isbn'):
                        st.write(f"**ISBN:** {book['isbn']}")
                    st.write("-" * 20)
            else:
                st.info(f"No books found matching '{query}'.")
        else:
            st.warning("Please enter a search query.")

def update_book():
    """Updates the information of an existing book."""
    st.subheader("Update Book")
    if not books:
        st.info("Your library is empty. Add some books first.")
        return

    titles = [book['title'] for book in books]
    selected_title = st.selectbox("Select a book to update:", titles)

    if selected_title:
        book_to_update = next((book for book in books if book['title'] == selected_title), None)
        if book_to_update:
            st.write(f"Updating: '{book_to_update['title']}' by {book_to_update['author']}")

            new_title = st.text_input(f"New title ({book_to_update['title']}):", value=book_to_update['title'])
            new_author = st.text_input(f"New author ({book_to_update['author']}):", value=book_to_update['author'])
            new_isbn = st.text_input(f"New ISBN ({book_to_update.get('isbn', 'None')}):", value=book_to_update.get('isbn', ''))
            new_genre = st.text_input(f"New genre ({book_to_update.get('genre', 'None')}):", value=book_to_update.get('genre', ''))
            new_publication_year = st.text_input(f"New publication year ({book_to_update.get('publication_year', 'None')}):", value=book_to_update.get('publication_year', ''))
            new_status = st.selectbox(f"New status ({book_to_update['status']}):", ["Available", "Borrowed", "Read"], index=["Available", "Borrowed", "Read"].index(book_to_update['status']))

            if st.button("Update Book"):
                updated_book = {
                    "title": new_title,
                    "author": new_author,
                    "isbn": new_isbn if new_isbn else None,
                    "genre": new_genre if new_genre else None,
                    "publication_year": new_publication_year if new_publication_year else None,
                    "status": new_status
                }
                index = books.index(book_to_update)
                books[index] = updated_book
                save_books(books)
                st.success("Book information updated successfully!")

def delete_book():
    """Deletes a book from the library."""
    st.subheader("Delete Book")
    if not books:
        st.info("Your library is empty. Nothing to delete.")
        return

    titles = [book['title'] for book in books]
    selected_title = st.selectbox("Select a book to delete:", titles)

    if selected_title:
        book_to_delete = next((book for book in books if book['title'] == selected_title), None)
        if book_to_delete:
            if st.button(f"Delete '{book_to_delete['title']}'?"):
                books.remove(book_to_delete)
                save_books(books)
                st.success(f"Book '{book_to_delete['title']}' deleted successfully!")

# Streamlit App Layout
st.title("Personal Book Library Manager")

books = load_books()

menu = st.sidebar.selectbox("Menu", ["Add Book", "View Books", "Search Book", "Update Book", "Delete Book"])

if menu == "Add Book":
    add_book()
elif menu == "View Books":
    view_all_books()
elif menu == "Search Book":
    search_book()
elif menu == "Update Book":
    update_book()
elif menu == "Delete Book":
    delete_book()