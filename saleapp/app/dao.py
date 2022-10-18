import json
from app import app

def load_categories():
    with open('%s/%s' % (app.root_path, 'data/categories.json'), encoding='utf-8') as f:
        return json.load(f)

def load_products():
    with open('%s/%s' % (app.root_path, 'data/products.json'), encoding='utf-8') as f:
        return json.load(f)

