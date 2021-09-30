from flask import Flask, render_template, request
import os.path
from data import News

result=["Linux","Open-Source","Android"]
Latest_News = News(result)

STATIC_DIR=os.path.abspath('static')
TEMPLATE_DIR=os.path.abspath('templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    Latest_News=News(result)
    return render_template('home.html',News=Latest_News,result=result)


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['keywords']
    result = [x.strip() for x in text.split(',')]
    Latest_News=News(result)
    return render_template('home.html',News=Latest_News,result=result)


if __name__ == '__main__':
    app.run(debug=True)
