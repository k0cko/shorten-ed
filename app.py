from flask import Flask, render_template, request, redirect
from sqlalchemy import insert, select
from db import engine, urls_table
from helpers import is_valid_short_code, generate_hash
import validators

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        if not url:
            # TODO ERROR
            return "error"
        
        if not bool(validators.url(url)):
            return "validation error"

        # Check if long url exists in the DB
        stmt = select(urls_table.c.short_code).where(urls_table.c.long_url == url)
        connection = engine.connect()
        result = connection.execute(stmt).first()

        if not result:
            # Add new long url to DB and return short code so we can give user shortened URL
            short_code = add_url(url) 
        else:
            short_code = result[0]
        
        # TODO show user new url
        return short_code

    return render_template("index.html")

@app.route('/<string:short_code>')
def redirect_to_url(short_code):
    if not is_valid_short_code(short_code):
        # TODO error
        return "error"

    # TODO redirect to long url
    stmt = select(urls_table.c.long_url).where(urls_table.c.short_code == short_code)
    connection = engine.connect()
    result = connection.execute(stmt).first()

    if not result:
        # TODO error
        return "error"

    return redirect(result[0])


def add_url(url):
    short_code = generate_hash()
    stmt = insert(urls_table).values(long_url=url, short_code=short_code)
    
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

    return short_code