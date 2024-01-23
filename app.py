from flask import Flask, render_template, request, redirect
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
        
        confirmation = "Your message has been sent!"
        
        return render_template('index.html', confirmation=confirmation)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()