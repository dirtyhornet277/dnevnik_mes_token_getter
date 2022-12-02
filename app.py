from flask import Flask, request
from finc import *
import time
app = Flask(__name__)

@app.route("/get_token", methods=["GET", "POST"])
def get_token_for_dnevnik():
    if request.method == "POST":
        login = request.json["login"]
        password = request.json["password"]
        data = get_token(login, password)

        return {"token":data}
    else:
        return {"message":"Use POST request"}

app.run(host="0.0.0.0")
