
# Library CRUD System

This Library CRUD System is small scaled Rest API based in Django Python.


## Installation

Install with the given GIT link above


    
## How to Start

- Firstly make sure you have Django and DjangoRestAPI.
    `pip install django djangorestframework`
- In Terminal, type `cd Library_CRUD_API`.
- Then type `py manage.py runserver` in the Terminal.
- Go to the website,
- **NOTE:- the page wont load directly, add `/books/` to the end of the website to get list of all the books.**
- You can only send POST and GET request to this `/books/`.
- You can send GET , PUT  , DELETE request to `/books/<int>/ ` for example:
    - GET request to `/books/1/` will return all the details of the book with `book_Id=1`.
    - PUT request to `/books/1/` will update the details of the book with `book_Id=1`.
    - DELETE request to `/books/1/` will delete the book object with `book_Id=1`.
    - **If the Id does not exist it will return not found error.**
- To send API requests, any API free tester in chrome webstore can be used, for testing this project **Talend API Tester** was used from Chrome Web Store.
## Authors

- [@Harsh Kothari](https://github.com/harshj3915)
