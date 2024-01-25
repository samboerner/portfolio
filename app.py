from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import app, mail
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO messages (name,email,message) VALUES (?,?,?)",
                        (name, email, message))
            db.commit()

        sendMail(name, email, message)    
        
    return render_template('index.html')


def sendMail(name, email, message):
    msg = Message(f"New Message from {name} on samboerner.com",
                  sender = "",
                  recipients=[""])
    
    msg.body = f"You have a new message.\nName: {name}\nEmail: {email}\nMessage: {message}"

    mail.send(msg)


if __name__ == '__main__':
    app.run()