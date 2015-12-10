"""This is a basic web server that's hosting a couple of basic url's. This web
server is used to check to see if the tests in the test application are used
correctly. Flask's implementation has been chosen almost completely because
it's what I know at the time of this writing.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/"):
    return "test_body"

if __name__ = "__main__":
    app.run("0.0.0.0", port=4000)
