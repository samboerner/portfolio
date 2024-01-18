from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder="static")

@app.route("/", methods=["GET","POST"])
def submit_form():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        api = "https://sheets.googleapis.com/v4/spreadsheets/1E2O5SFWq6ntAIbL59YzdnpAnf2JcYBccON8vmxIAbQ0/values/Sheet1?key=AIzaSyCZFnYLz__w-0P4lLKEA--6JvTf7awjOms"

        data = {
            "values": [[name, email, message]]
        }

        response = requests.post(api, json=data)

        confirmation = ""
        if response.status_code == 200:
            confirmation = "Your message has been sent!"
        else:
            confirmation = "Error submitting form"

        return render_template("index.html", confirmation=confirmation)
    else:
        return render_template("index.html")
    