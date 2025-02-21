import random
import string
import re

def generate_hash():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

def is_valid_short_code(short_code):
    """Ensure short_code is alphanumeric (avoids SQL injection)"""
    return bool(re.fullmatch(r"[a-zA-Z0-9]+", short_code))
