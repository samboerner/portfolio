from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Configuration for Flask Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('DEFAULT_SENDER')

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Form submission from the contact section
    if request.method == 'POST':
        # Retrieve data from form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Send email from form submission
        msg = Message(f"New Message from {name} on SamBoerner.com",
                        recipients=[os.getenv('MAIL_RECIPIENT')])
        msg.body = f"You have a new message.\nName: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)       
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run()