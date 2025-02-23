from flask import Flask, render_template, request, redirect, abort
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
            return render_template("error.html", error="Please provide URL")
        
        if not bool(validators.url(url)):
            return render_template("error.html", error="Invalid URL")

        # Check if long url exists in the DB
        stmt = select(urls_table.c.short_code).where(urls_table.c.long_url == url)
        connection = engine.connect()
        result = connection.execute(stmt).first()
        connection.close()

        if not result:
            # Add new long url to DB and return short code so we can give user shortened URL
            short_code = add_url(url) 
        else:
            short_code = result[0]
        
        return render_template("success.html", shortened_url=request.url + short_code)

    return render_template("index.html")

@app.route('/<string:short_code>')
def redirect_to_url(short_code):
    if not is_valid_short_code(short_code):
        abort(404)

    # Reduirect to long url
    stmt = select(urls_table.c.long_url).where(urls_table.c.short_code == short_code)
    connection = engine.connect()
    result = connection.execute(stmt).first()
    connection.close()
    
    if not result:
        abort(404)

    return redirect(result[0])


def add_url(url):
    with engine.connect() as conn:
        short_code = generate_hash(conn)
        stmt = insert(urls_table).values(long_url=url, short_code=short_code)
        conn.execute(stmt)
        conn.commit()

    return short_code