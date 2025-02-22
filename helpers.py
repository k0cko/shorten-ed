import random
import string
import re
from sqlalchemy import select
from db import urls_table

def generate_hash(connection):
    while True:
        hash = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        stmt = select(urls_table.c.short_code).where(urls_table.c.short_code == hash)
        result = connection.execute(stmt).first()

        if not result:
            return hash



def is_valid_short_code(short_code):
    """Ensure short_code is alphanumeric (avoids SQL injection)"""
    return bool(re.fullmatch(r"[a-zA-Z0-9]+", short_code))
