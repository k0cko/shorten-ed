# shorten.ed
### Video Demo:
### Description:
__shorten.ed__ is a simple URL shortener built using Flask and SQLite. The application allows users to shorten long URLs into shareable links and provides redirection when the short link is accessed.

This project was developed as part of my __CS50 Final Project__.

## File explanation:
- __static/__ Contains index page JS file and logo img
- __templates/__ Contains the page templates
- __.gitignore__ Describes the files and folders that should not be version controlled
- __requirements.txt__ Installs project dependencies
- __app.py__ Main app file. Handles app routing, creation of new shortened URLs etc.
- __db.py__ Creates connection to the DB. Creates table if it doesn't exist, and also indexes the long_url and short_code fields of the table, because they're heavily used in order to search for short_code or to check if long_url is already in the DB
__helpers.py__ Contains helper functions.

## Features:
- __Shorten Long URLs__: Converts long URLs into short, easy-to-share links
- __Asynchronouse Update__: Page is updated asynchronously through JavaScript using Fetch API

## Future Improvements:
- __Link Expiry__: Automatically delete shortened URLs that are 30 days old using CRON

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