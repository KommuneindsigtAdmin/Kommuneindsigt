from flask import Flask

app = Flask(__name__)

@app.route("/")
def hjem():
    return "Velkommen til min kommuneside!"

if __name__ == "__main__":
    app.run()
