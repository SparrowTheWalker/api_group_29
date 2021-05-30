from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///group.db'
db = SQLAlchemy(app)

class data(db.Model):
   id = db.Column(db.Integer, primary_key = True,)
   fname=db.Column(db.String(30), nullable=False)
   lname=db.Column(db.String(30), nullable=False)
   email=db.Column(db.String(20), nullable=False)
   message=db.Column(db.String(200), nullable=False)

   def __init__(self, fname, lname, email, message):
      self.fname=fname
      self.lname=lname
      self.email=email
      self.message=message

@app.route('/insert', methods = ['POST','GET'])
def insert_data(): 
   # return request.form
   if request.method == 'POST': 
      fname=request.form['fname']
      lname=request.form['lname']
      email=request.form['email']
      message=request.form['message']


      ins_data = data(fname,lname,email,message)
      db.session.add(ins_data)
      db.session.commit()
      
      return render_template("contact.html")

@app.route("/")
def home():
   return redirect("/index.html")

@app.route("/index.html")
def homee():
   return render_template("index.html")

@app.route("/portfolio-page.html")
def port():
   return render_template("portfolio-page.html")

@app.route("/portfolioII-page.html")
def port_1():
   return render_template("portfolioII-page.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route('/home')
def index():
    return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True)
    