# shorten.ed
### Video Demo:
### Description:
__shorten.ed__ is a simple URL shortener built using Flask and SQLite. The application allows users to shorten long URLs into shareable links and provides redirection when the short link is accessed.

This project was developed as part of my __CS50 Final Project__.

### File explanation:

## - __static/__:

- __index.js__:
This file updates the page asynchronously using Fetch API. It waits for the DOM to load, then binds to the shorten button and adds a click event to it. Then preventDefault and stopPropagation methods ot the event object are called to stop the page from redirecting. Then updatePage function is called, where POST request is made to the page and form data is send to be checked by the back-end. Then we wait for response, and if the response is 200 we update the page with the response.

## - __templates/__ Contains the page templates
## - __.gitignore__ Describes the files and folders that should not be version controlled
## - __requirements.txt__ Installs project dependencies
## - __app.py__ Main app file. Handles app routing, creation of new shortened URLs etc.

- __index__: Function that renders index html if the request method is GET. If the request is POST, checks if there's a URL posted, or if the URL is valid using the "validator" library and returns the success.html template if everything is valid, else returns the error.html

- __redirect_to_url__: Function that checks if the short code that comes after the '/' is valid. If it is, we get the corresponding long_url from the DB and we redirect the user, else if no result we abort with error 404

- __add_url__: Function inserts new records in the DB

## - __db.py__ Creates connection to the DB. Creates table if it doesn't exist, and also indexes the long_url and short_code fields of the table, because they're heavily used in order to search for short_code or to check if long_url is already in the DB
## __helpers.py__ Contains helper functions.

- __generate_hash__: Function that is wrapped in infinite loop and in it it creates random 8 digit long hash, then checks if a record with the generated hash exists in the DB and continues to do so until a unique hash is created, then returns it.

- __is_valid_short_code__: Function that checks if the short code that's trying to be accessed by the user contains only alphabet characters and digits

## Features:
- __Shorten Long URLs__: Converts long URLs into short, easy-to-share links
- __Asynchronouse Update__: Page is updated asynchronously through JavaScript using Fetch API

## Future Improvements:
- __Link Expiry__: A necessary update of the app would be to have links expire after certain days. The problem with the current app is that if it scales, and is being used a lot daily, at one moment the database would get way too big, with most records unused, since most people need to shorten a url that will be used 1-2 times. A way to handle this would be to have CRON job, that executes everyday, that checks if there are records that were created before for example 30 days, and deletes them. This way the database would be free of unused records. We would have to add new 'created' field in the 'urls' table, and set all of the current records to the current date, so that the cron deletes them after 30 days. 

## Installation Instructions:

To run this project locally, follow these steps:

### Clone the repository:

```sh
git clone https://github.com/k0cko/shorten-ed.git
cd shorten-ed
```

### Create & Activate Virtual Environment

```sh
 python -m venv .venv
 source .venv/bin/activate  # Linux/macOS
 .venv\Scripts\activate    # Windows
```

### Install Dependencies

```sh
 pip install -r requirements.txt
```

### Run the Application

```sh
 flask run
```

The server will start at `http://127.0.0.1:5000/`.

## Usage Guide

### Shorten a URL

1. Open the web app.
2. Enter a long URL in the input field.
3. Click __Shorten__.
4. The app will generate a short link (e.g., `http://127.0.0.1:5000/abc123`).
5. Paste the short link in your browser, and it will redirect you to the original URL

## Technologies Used

- __Flask__ - Web framework for Python
- __SQLite__ - Lightweight database for storing URLs
- __SQLAlchemy Core__ - Database connection and queries
- __Jinja2__ - HTML templating engine for Flask
- __Bootstrap__ - Frontend styling for responsiveness
- __JavaScript__ - Frontend asynchronous update