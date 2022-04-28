from flask import Flask
app = Flask(__name__)  #procifile app(file name):app (app = flask)

@app.route("/")
def home():
    return "hello"

@app.route("/test")
def page2():
    return "this is test"

if __name__ == "__main__":
    app.run()