from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return "Create a Story Page"

@app.route('/join')
def join():
    return "Join a Story Page"

@app.route('/about')
def about():
    return "About Page"

@app.route('/contact')
def contact():
    return "Contact Page"

if __name__ == '__main__':
    app.run(debug=True)
