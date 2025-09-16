from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_admin import Admin

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__) 
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assets.db"
# initialize the app with the extension
db.init_app(app)

class Asset(Base):
    __tablename__ = 'assets'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(200))                                       

@app.route('/') 
def home(): 
    return render_template('index.html', title='My Home Page')

@app.route('/about') 
def about():
    return render_template('about.html', title='About Us')

@app.route('/assets') 
def assets():
    return render_template('assets.html', title='Assets')

admin = Admin(app, name='microblog', template_mode='bootstrap3')

if __name__ == '__main__': 
    app.run(debug=True)
