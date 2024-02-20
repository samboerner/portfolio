from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()
application = Flask(__name__)

# Configuration for Flask Mail
application.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
application.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
application.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
application.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
application.config['MAIL_DEFAULT_SENDER'] = os.getenv('DEFAULT_SENDER')

mail = Mail(application)

@application.route('/', methods=['GET', 'POST'])
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
    application.run()