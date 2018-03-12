from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    title = "index"
    return render_template("index.html", title=title)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
