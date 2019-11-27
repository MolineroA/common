from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    title = 'Home'
    return render_template("home.html", data=get_data(), title=title)


@app.route('/<product>')
def get_product(product):
    title = product
    for p in get_data():
        if p.get('title') == product:
            data = p.get('text')
            return render_template('products.html', product=product, data=data, title=title)


@app.route('/author')
def get_author():
    title = 'Author'
    return render_template('author.html', title=title)


if __name__ == "__main__":
    app.run(debug=True)
