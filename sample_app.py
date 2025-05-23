# Add to this file for the sample app lab  id: 55e401f7bdcd password:  62955146070f4db9864d8b2648a99621  root@4671de257ed2
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)
