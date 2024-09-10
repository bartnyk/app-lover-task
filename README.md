# Library Management System

This is a Django Rest Framework application for managing a library.

## Models

- `Book`: Represents a book in the library. Each book has a title, author, and publication date.
- `Rent`: Represents a book rental. Each rental has a book, a library card number, a rent date, and a return date.

## API Endpoints

- `GET /library/books/<id>/`: Retrieve a book by its ID.
- `GET /library/books/`: Get a list of all books.
- `POST /library/books/<id>/rent/`: Rent a book. The book is identified by its ID.
- `POST /library/books/<id>/return/`: Return a rented book. The book is identified by its ID.
- `DELETE /library/books/<id>/`: Delete a book by its ID.

## Setup

> **NOTE:** You need to have Docker/Docker Desktop installed on your machine to run this application.

1. Clone the repository: `git clone git@github.com:bartnyk/app-lover-task.git`
2. Navigate to the project directory: `cd app-lover-task`
3. Run the application: `docker-compose up`
