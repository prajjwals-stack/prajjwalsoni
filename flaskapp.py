from flask import Flask, render_template, request , redirect
import sqlite3
app=Flask(__name__)


@app.route('/')
def users():
    connect=sqlite3.connect('IOT-Project.db')
    c=connect.cursor()
    c.execute('SELECT * FROM ReadThingspeak')
    data_fetch=c.fetchall()
    return render_template("index.html",data_fetch=data_fetch)
if __name__ =='__main__':
    app.run(debug =True)    