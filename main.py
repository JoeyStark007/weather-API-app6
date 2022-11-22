from flask import Flask, render_template
import pandas as pd

# Create website object
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv("")
    temperature = 21
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "  main  ":
    app.run(debug=True)
