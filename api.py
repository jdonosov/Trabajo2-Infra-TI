import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("indexEmpty.html")

@app.route("/profile/genes/")
def profile():
    return render_template("indexEmpty.html")

@app.route("/profile/genes/<geneName>/")
def getGenes(geneName):
    #genes = ["RPS27L", "TSPAN6", "ENPP4", "C4orf27", "WSCD2"]
    resp = requests.get("https://www.genenetwork.nl/api/v1/gene/" + geneName + "/",
                        headers={'Accept': 'application/json'})

    data = resp.json()

    return render_template("index.html", geneData=data)

if __name__ == "__main__":
    Flask.run(app)
    #Flask.run(app, host="0.0.0.0", port=80)