from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template('home.html')


@app.route('/vegetables')
def get_vegetable():
    vegetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', vegetables=vegetables)


@app.route('/fruits')
def get_fruits():
    fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', fruits=fruits)


if __name__ == "__main__":
    app.run(debug=True)
