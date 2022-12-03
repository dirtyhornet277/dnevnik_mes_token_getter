from flask import Flask, request, render_template
from finc import *
import time
app = Flask(__name__)

@app.route("/get_token", methods=["GET", "POST"])
def get_token_for_dnevnik():
    if request.method == "POST":
        login = request.form["login"]
        print(login)
        password = request.form["password"]
        data = get_token(login, password)["value"]

        return render_template("index.html", token=data)
    else:
        return render_template("index.html")

app.run(host="0.0.0.0")
