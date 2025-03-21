from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/xzyhellsing")
def xzyhellsing():
    return "POC xzyhellsing subdomain takeover <a href='https://hackerone.com/xzyhellsing?type=user'>https://hackerone.com/xzyhellsing?type=user</a>"

if __name__ == "__main__":
    app.run(debug=True)
