import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/run")
def run():
    cmd = request.args.get("cmd")  # this is vulnerable
    os.system(cmd)  # 🚨 This is the vulnerability CodeQL detects!
    return "Command executed"

if __name__ == "__main__":
    app.run(debug=True)
