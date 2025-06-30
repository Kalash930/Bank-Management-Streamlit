import json
import random
from pathlib import Path

DATABASE = 'data.json'


def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, 'r') as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATABASE, 'w') as f:
        json.dump(data, f, indent=4)


def generate_account_number(existing):
    while True:
        acc = str(random.randint(10**9, 10**10 - 1))
        if all(acc != user["accountNo"] for user in existing):
            return acc


def find_user(account_no, pin, data):
    return next((u for u in data if u['accountNo'] == account_no and str(u['pin']) == pin), None)
