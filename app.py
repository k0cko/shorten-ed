from flask import Flask, render_template, request
import string
import random
from sqlalchemy import insert
from db import engine, urls_table

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        if not url:
            # TODO ERROR
            return "error"

        # TODO check if url exists in database

        add_url(url)

    return render_template("index.html")

def add_url(url):
    with engine.connect() as conn:
        stmt = insert(urls_table).values(long_url=url, short_code=generate_hash())
        
        # TODO


def generate_hash():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))