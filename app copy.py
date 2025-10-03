from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from flask_admin import Admin
import sqlite3

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
@app.route('/data')
def data():
    return render_template('data.html', title='Data Page')
    conn = sqlite3.connect('eb2.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255))""")
    # Insert data into the table
    cursor.execute("INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')")
    cursor.execute("INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')")
    cursor.execute("INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')"
    )
    print("Data Inserted in the table: ")
    cursor.execute("SELECT * FROM STUDENT")
    for row in cursor.fetchall():
        print(row)
    return "Data inserted and displayed in console"

admin = Admin(app, name='microblog', template_mode='bootstrap3')

if __name__ == '__main__': 
    app.run(debug=True)
