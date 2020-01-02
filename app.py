from flask import Flask, render_template
import os.path
from data import News

News = News()

STATIC_DIR=os.path.abspath('static')
TEMPLATE_DIR=os.path.abspath('templates')


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    return render_template('home.html',News=News)

if __name__ == '__main__':
    app.run()
