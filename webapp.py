#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Syria
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : Open Source
# -----------------------------------------------------------------------------
# Creation : 24-Sep-2013
# Last mod : 24-Sep-2013
# -----------------------------------------------------------------------------

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "build":
            from flask_frozen import Freezer
            freezer = Freezer(app)
            freezer.freeze()
        exit()
    app.debug = True
    app.run(host='0.0.0.0')


# EOF
