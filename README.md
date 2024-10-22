# UNIT-1-PROJECT: Abjad Library

## Overview
Abjad is an interactive Command Line Interface (CLI) application that allows users to engage with a diverse collection of books. This library has two main user types: Admin and Viewer. Each user can perform specific tasks to facilitate the management and exploration of books.

### User Stories
As a **Viewer**, I should be able to:
- Browse books available in the library.
- View detailed information about each book (title, author, description, likes, comments, ratings, Average Rating).
- Search for specific books by the book ID.
- Like my favorite books.
- Leave comments on the books.
- Rate the books on a scale from 1 to 5.

As an **Admin**, I should be able to:
- Add new books to the library.
- Remove books from the library.
- List all available books in the library.

## Usage
To use Abjad, follow these instructions:

### For Viewer:
- Type `list` to browse all books.
- Type `view` then `book_id` to see detailed information about a specific book.
- Type `comment` then `book_id` then `Your Comment` to leave feedback on a book.
- Type `like` then `book_id` to like a book.
- Type `rate` then `book_id` then `rating` to rate a book.
- Type `logout` to log out from admin mode.

### For Admin:
- Type `list` to list all books.
- Type `add` to add a new book.
- Type `remove` then `book_id` to delete a book from the library.
- Type `logout` to log out from admin mode.