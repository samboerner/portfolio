from flask import Flask, render_template, request
from flask_mail import Mail, Message
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

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
        
        msg = Message(f"New Message from {name} on samboerner.com",
                        recipients=[os.getenv('MAIL_RECIPIENT')])
    
        msg.body = f"You have a new message.\nName: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)       
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run()