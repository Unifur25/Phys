from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sympy as sp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI' ]= 'sqlite:///myproject.db'
db = SQLAlchemy(app)



class Post(db.Model):
  id = db.Column (db.Integer,primary_key=True)
  title = db.Column(db.String(300), nullable=False)
  text = db.Column(db.Text,nullable=False)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/form")
def form():
    return render_template('form.html',methods=['POST'])


@app.route("/mater")
def mater():
    return render_template('mater.html')


@app.route("/zakon")
def zakon():
    return render_template('zakon.html')





@app.route("/about",methods=['GET','POST'])
def about():
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        try:

            result = str(sp.sympify(expression).evalf())
        except Exception as e:
            result = f'Ошибка: {str(e)}'

    return render_template('about.html', result=result)



    

 



if __name__ == "__main__":
    app.run(debug=True)