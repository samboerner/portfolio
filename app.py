from flask import Flask, render_template, request
from oauth2client.service_account import ServiceAccountCredentials
import gspread

app = Flask(__name__, static_folder="static")

# Setting up Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

@app.route("/", methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        # Extract data from HTML form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Authenticate with Google Sheets
        gc = gspread.authorize(creds)
        sheet = gc.open('Messages').sheet1

        #Write data to Google Sheet
        sheet.append_row([name, email, message])

        confirmation = "Your message has been sent!"

        return render_template("index.html", confirmation=confirmation)
    else:
        return render_template("index.html")
    